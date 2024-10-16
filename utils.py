"""
Functions to download price data from Yahoo Finance
"""
import pandas as pd
from typing import List, Dict
from datetime import datetime, timedelta
from sqlalchemy import create_engine
import yfinance as yf


# Univariate retrievals (one ticker)
def retrieve_yahoo_prices_and_volume(
    ticker: str = 'spy', start_date: str = None, end_date: str = None
) -> Dict:
    """
    Retrieves the open, high, ñopw and close price
    time series from Yahoo Finance.

    Args:
        ticker (str): Ticker to retrieve (default 'spy').
        start_date (str): Start date of the time series (format 'YYYY-MM-DD').
            Defaults to 5 years before the end date if not provided.
        end_date (str): End date of the time series (format 'YYYY-MM-DD'). 
            Defaults to yesterday's date if not provided.

    Returns:
        pd.Series: Time series of close prices.
    """
    # Set end_date to yesterday if not provided
    if end_date is None:
        end_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

    # Set start_date to 5 years before the end_date if not provided
    if start_date is None:
        end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
        start_date = (end_date_obj - timedelta(days=5*365)).strftime('%Y-%m-%d')

    try:
        yahoo_data = yf.Ticker(ticker)
        print(f"Processing Open, High, Low, Close for {ticker}")
        price_df = yahoo_data.history(
            start=start_date, end=end_date)[['Open', 'High', 'Low', 'Close', 'Volume']]
        
        price_df.columns = [col.lower() for col in price_df.columns]
        price_df.index.name = 'time'

        if price_df.empty:
            raise Exception("No Prices.")
        return {'ticker': ticker, 'prices': price_df}
    except Exception as ex:
        print(f"Sorry, Data not available for '{ticker}': Exception is {ex}")



def populate_etf_tables(
    tickers: list, db_connection_string: str, 
    start_date: str = None, end_date: str = None
):
    """
    Populates individual tables in the SQLite database for each ticker's price and volume data.

    Args:
        tickers (list): List of tickers (e.g., constituents of an ETF).
        db_connection_string (str): Database connection string.
        start_date (str): Start date for data retrieval.
        end_date (str): End date for data retrieval.
        
    Example usage
        database_connection_string = 'sqlite:///etf_test.db'
        etf_tickers = ['GDOT', 'GS', 'PYPL', 'SQ']
        populate_etf_tables(etf_tickers, database_connection_string)
    """
    # Create a connection to the database
    engine = create_engine(db_connection_string)
    
    for ticker in tickers:
        print(f"\nProcessing data for {ticker}...")
        data = retrieve_yahoo_prices_and_volume(
            ticker, start_date, end_date)
        if data is not None:
            price_data = data['prices']
            ticker = data['ticker']
            sql_table_name = ticker
            price_data.to_sql(
                sql_table_name, con=engine, if_exists='replace', index=True)
            print(f"Data for {ticker} stored in table '{sql_table_name}'")
        else:
            print(f"No data available for {ticker}")