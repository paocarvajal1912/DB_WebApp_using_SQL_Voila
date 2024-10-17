# DB WebApp using SQL and Voila

## Introduction

ETFs are popular financial instruments due to their diversification and low costs. Since ETFs are composed of multiple securities, analyzing their performance requires managing diverse data.

In this project, we build a financial database and web application using SQL, Python, and the Voilà library to analyze ETF performance. We use Yahoo Finance API to download market data, and store it in a SQL database. We query the data, construct the ETF, visualize its performance, and save equally-weighted ETF returns.

A [video of a simpler version](https://www.youtube.com/watch?v=wyaDnec7fGk) is included to demonstrate how easily Voilà can export interactive visualizations and text to a web interface.

---

## Project Description

In this project, we develop a **financial database** and a **web application** to analyze the performance of a hypothetical FinTech **Exchange-Traded Fund (ETF)**. The application is built using **SQL**, **Python**, and the **Voilà** library. The ETF comprises four stocks: **GDOT** (Green Dot Corporation), **GS** (Goldman Sachs), **PYPL** (PayPal Holdings), and **SQ** (Block, formerly Square). Each stock has its own dedicated table within the `etf.db` database. Data is downloaded using Yahoo Finance API.

The analysis focuses on the **daily returns** of the individual ETF stocks, as well as the performance of the ETF as a whole. Once the analysis is complete, the visualizations are deployed to a web application using the Voilà library, which allows us to transform the Jupyter Notebook into an interactive web interface.

---

### Project Outline

The project is structured into several key parts:

0. **Populating Data into SQL Database**
   - We begin by preparing the data. First, we define the tickers that make up the Fintech ETF and populate a SQL database with the relevant market data using the Yahoo Finance API. Next, we add the daily returns to the created SQL database. The functions to perform these tasks are stored in `utils.py`.

1. **Analyze a Single Asset in the ETF**
   - In this section, we perform individual analysis on a selected stock in the ETF. This includes calculating daily returns, visualizing the stock's performance, and understanding its contribution to the overall ETF.

2. **Optimize Data Access with Advanced SQL Queries**
   - Here, we focus on improving the efficiency of data access. By writing additional SQL queries, we can retrieve and process stock data more efficiently, which is crucial for optimizing performance, especially when handling large datasets.

3. **Analyze the ETF Portfolio**
   - This part involves analyzing the ETF as a whole, combining the data of all four stocks. We compute the overall daily returns and provide insights into the performance of the ETF as a portfolio.

4. **Create a New Database for Equal-Weighted ETF Returns**
   - In order to preserve the original data, we create a new database to store the daily returns of the ETF, assuming the stocks are equally weighted. This ensures that the original `etf.db` database remains unaltered while we perform further analysis.

5. **Deploy the Notebook as a Web Application**
   - Finally, we use the **Voilà** library to deploy the Jupyter Notebook as a web application. This step allows users to interact with the analysis through a browser-based interface, enabling real-time exploration of the ETF data and visualizations.

---

## Technologies
For this project, we use a **Jupyter notebook** running Python 3.7 or higher, **SQL** in a PyViz environment ecosystem for visualizations, and the **Voila** library to construct a web application from the analysis. We also use the following specific libraries:
* `Pandas`, and `Numpy`  for calculations; 
* `Hvplot` for visualizations; 
* `Sqlalchemy` for the connection and access to a SQL database; 
* `Datetime` for the management of datetime data and indexes. 


---

## Installation Guide

This project is built in a Jupyter Notebook. If you don’t have Jupyter installed, you can follow the instructions [here](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html) to set it up.

### Required Libraries

You can install all the necessary libraries by using the provided `requirements.txt` file. To install the dependencies, follow these steps:

1. **Download the `requirements.txt` file** included in the project repository.
2. Open a terminal and navigate to the project directory where the `requirements.txt` file is located.
3. Run the following command to install all the required packages:

   ```bash
   pip install -r requirements.txt
   ```

This will install the following libraries:
- **`numpy`**: For numerical computations.
- **`pandas`**: For data manipulation and DataFrame operations.
- **`hvplot`**: For creating interactive visualizations.
- **`sqlalchemy`**: For connecting and interacting with the SQL database.

### Manually Installing Specific Libraries (If Needed)

If you'd like to manually install any missing libraries, here are the installation commands:

- **SQLAlchemy**:
  ```bash
  pip install SQLAlchemy
  ```

- **Voilà** (optional for deploying as a web app):
  ```bash
  conda install -c conda-forge voila
  ```

Once the required packages are installed, you’ll be ready to run the project.

---

### Usage

The main file is the ``etf_analyzer.ipynb`` Jupyter Notebook with a pre-run code. You can go through it and see code as well as results. 

If you look to reuse the code, and do not have experience on jupyter lab, please refer:
https://www.dataquest.io/blog/jupyter-notebook-tutorial/

Some of the visualizations have interactions available. To see some of the interactions, and how you can see this analysis on a web environment using Voila Library, you can take a look to [this video](https://www.youtube.com/watch?v=wyaDnec7fGk).

---

## Contributors
This project was coded by Paola Carvajal Almeida, paola.antonieta@gmail.com.

Contact email: paola.antonieta@gmail.com
LinkedIn profile: https://www.linkedin.com/in/paolacarvajal/

---


## License
This project uses a MIT license. This license allows you to use the licensed material at your discretion, as long as the original copyright and license are included in your work files. This license does not contain a patent grant,  and liberate the authors of any liability from the use of this code.
