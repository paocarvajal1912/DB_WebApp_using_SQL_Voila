# DB_WebApp_using_SQL_Voila

Nowadays, ETFs are one of the more common and appreciated financial instruments. This, because of their diversification attibutes, and their low cost characteristics. ETFs are composed by several securities, so it is required to manage multiple security data in order to analyzed their performance.

In this project we build a financial database and web application by using SQL, Python, and the Voila library to analyze an ETF performance. We ewill apply several queries to access the data, as well as construct the ETF and visualize its performance. A video is included to see how simple the Voila Library can be used to export interactive visualization, as well as text, to a web environment.


## Technologies
For the analysis we use a jupyter notebook, Python 3.7, and SQL in a PyViz environment ecosystem for visualizations, and the Voila library to construct a web application from the analysis. We also use the following specific libraries:
Pandas, and Numpy  for calculations; Hvplot for visualizations; Sqlalchemy for the connection and access to a SQL database; Datetime for the management of datetime data and indexes. 


## Instalation Guide
The file is a jupyter notebook. If you don't have jupyter notebook, you can install it following the instruction here:

https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html

To see if you have SQLAlchemy, you can use:

``conda list sqlalchemy``


If the package doesn't appear displayed on your terminal, you can install it by using:
``pip install SQLAlchemy``

For the installation of voila you can use conda:
``conda install -c conda-forge voila``


### Usage

The main file is the ``etf_analyzer.ipynb`` Jupyter Notebook with a pre-run code. You can go through it and see code as well as results. 

If you look to reuse the code, and do not have experience on jupyter lab, please refer:
https://www.dataquest.io/blog/jupyter-notebook-tutorial/

Some of the visualizations have interactions available. To see some of the interactions, and how you can see this analysis on a web environment using Voila Library, you can take a look to [this video](Voila_Recording.mov) in the same folder than this README file.
``Voila_Recording.mov``



## Contributors
This project was coded by Paola Carvajal Almeida, paola.antonieta@gmail.com.

Contact email: paola.antonieta@gmail.com
LinkedIn profile: https://www.linkedin.com/in/paolacarvajal/


## License
This project uses a MIT license. This license allows you to use the licensed material at your discretion, as long as the original copyright and license are included in your work files. This license does not contain a patent grant,  and liberate the authors of any liability from the use of this code.
