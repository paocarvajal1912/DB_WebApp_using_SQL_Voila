"""
Functions to manage updates of etf tickers' data from Yahoo Finance
"""
import logging
import pandas as pd
from typing import List, Dict
import datetime as dt
from dateutil.relativedelta import relativedelta
import sqlalchemy
import yfinance as yf

def setup_logging(log_level: str = 'INFO'):
    """
    Configures the logging level based on user input.

    Args:
        log_level (str): Logging level ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
    """
    logging.basicConfig(
        level=log_level.upper(),  # Directly use the string level
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('etf_population.log', mode='w'),  # Overwrite log file each time
            logging.StreamHandler()
        ]
    )

# Univariate retrievals (one ticker)
def retrieve_yahoo_prices_and_volume(
    ticker: str = 'spy', start_date: str = None, end_date: str = None,
    cols: List = ['Open', 'High', 'Low', 'Close', 'Volume']
    ) -> Dict:
    """
    Retrieves a list of prices/volume data from Yahoo Finance.

    Args:
        ticker (str): Ticker to retrieve (default 'spy').
        start_date (str): Start date of the time series (format 'YYYY-MM-DD').
            Defaults to 5 years before the end date if not provided.
        end_date (str): End date of the time series (format 'YYYY-MM-DD'). 
            Defaults to yesterday's date if not provided.
        cols (list): columns to retrieve. Default to ['Open', 'High', 'Low', 'Close', 'Volume']

    Returns:
        a dictionary with:
            ticker: the name of the ticker
            data: a pd.Dataframe with columns cols
    """
    # Set end_date to yesterday if not provided
    if end_date is None:
        end_date = (dt.datetime.now().date() - dt.timedelta(days=1))
    # Set start_date to 5 years before the end_date if not provided
    if start_date is None:
        start_date = end_date - relativedelta(years=5)

    try:
        yahoo_data = yf.Ticker(ticker)
        logging.debug(f"Processing {cols} for {ticker}")
        data_df = yahoo_data.history(
            start=start_date, end=end_date)[cols]

        data_df.columns = [col.lower() for col in data_df.columns]
        data_df.index.name = 'time'

        if data_df.empty:
            raise Exception(f"No {cols} data for {ticker}.")
        return {'ticker': ticker, 'market_data': data_df}
    except Exception as ex:
        logging.error(f"Sorry, Data not available for '{ticker}': Exception is {ex}")
        return None


def store_market_data_to_sql(
    tickers: list, db_connector_string: str, 
    start_date: str = None, end_date: str = None
):
    """
    Populates individual tables in the SQLite database for each 
    ticker's price and volume data.

    Args:
        tickers (list): List of tickers (e.g., constituents of an ETF).
        db_connection_string (str): Database connection string.
        start_date (str): Start date for data retrieval.
        end_date (str): End date for data retrieval.
        log_level(str): Logging level 
            ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'). 
            Default to 'INFO'
        
    Example usage
        database_connection_string = 'sqlite:///etf_data.db'
        etf_tickers = ['GDOT', 'GS', 'PYPL', 'SQ']
        populate_etf_tables(etf_tickers, database_connection_string)
    """
    # Create a connection to the database
    engine = sqlalchemy.create_engine(db_connector_string)
    
    for ticker in tickers:
        logging.debug(f"\nProcessing data for {ticker}...")
        data = retrieve_yahoo_prices_and_volume(
            ticker, start_date, end_date)
        if data is not None:
            market_data = data['market_data']
            ticker = data['ticker']
            sql_table_name = ticker
            market_data.to_sql(
                sql_table_name, con=engine, if_exists='replace', index=True)
            logging.debug(f"Data for {ticker} stored in table '{sql_table_name}'")
            logging.debug(f"\n{market_data.head()}")
        else:
            print(f"No data available for {ticker}")
    logging.info("Completed retrieval of Market Data and Update of listed SQL-Tables.")
    populated_tables = sqlalchemy.inspect(engine).get_table_names()
    
    return populated_tables


def get_and_store_returns_to_sql(db_connector_string: str, ticker_tables: List[str],
    daily_ret_col_name: str = None) -> bool:
    """
    Add daily returns to a database of market data.

    Args:
        connector_string (str): Database connection string.
        ticker_tables (List[str]): List of table names for the tickers in the database.
        daily_ret_col_name (str): The name of the new daily return column.
            If set to None it will be 'daily_return'

    Returns:
        bool: True if the process is successful.
    """

    engine = sqlalchemy.create_engine(db_connector_string)

    if daily_ret_col_name is None:
        daily_ret_col_name = 'daily_return'
        
    for table in ticker_tables:
        logging.debug(f"Processing {table} for daily returns")

        # Retrieve the market data from the database
        query = f"SELECT * FROM {table}"
        market_data = pd.read_sql(query, con=engine, index_col='time')

        if market_data.empty:
            logging.warning(f"No data available in table {table}")
            continue

        market_data[daily_ret_col_name] = market_data['close'].pct_change()

        market_data.to_sql(table, con=engine, if_exists='replace', index=True)
        logging.debug(f"Daily returns calculations stored for SQL-table {table}")

    logging.info(f"Included/updated daily returns in listed SQL-tables.")
    return ticker_tables
