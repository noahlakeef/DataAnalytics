import pandas as pd
import pathlib as Path
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tk

def descriptiveStatistics(df):
    print('Conducting descriptive statistics on the dataset')
    
    info = df.describe()
    
    for index, row in info.items():
        print('\nColumn: ', index)
        print('Statistics: ')
        
        for col, val  in row.items():
            print('   ', col, ':',round(val, 2))
        
        #visualizingData(df, index)

def barChart(data):
    print('Enter column you would like to see a barchart for for')
    col = input('CPI, Debt, FEDFUNDS, GDP, MORTGAGE30US, NASDAQ, S&P500, UNRATE: ').upper()
    y = data[col]
    x = data['DATE']

    fig, ax = plt.subplots(1,1)
    ax.plot(x,y)
    plt.ylabel(col)
    plt.xlabel('Time')
    ax.xaxis.set_major_locator(tk.MultipleLocator(49))
    plt.show()

def showHist(data):
    print('Enter column you would like to see a histogram for')
    col = input('CPI, Debt, FEDFUNDS, GDP, MORTGAGE30US, NASDAQ, S&P500, UNRATE: ').upper()

    plt.hist(data[col])
    plt.xlabel(col)
    plt.show()

def lineCharts(data):
    data.plot.line(subplots = True)

def plot2Columns(data):
    print('Enter column for the Y axis')
    col = input('CPI, Debt, FEDFUNDS, GDP, MORTGAGE30US, NASDAQ, S&P500, UNRATE: ').upper()
    print('Enter column for the X axis')
    col2 = input('CPI, Debt, FEDFUNDS, GDP, MORTGAGE30US, NASDAQ, S&P500, UNRATE: ').upper()
    y = data[col]
    x = data[col2]

    fig, ax = plt.subplots(1,1)
    ax.plot(x,y)
    plt.ylabel(col)
    plt.xlabel(col2)
    plt.show()

print('Reading in Financial Dataframe: ')
dataframe = pd.read_csv(r'C:\DataAnalytics\DataAnalytics\DescriptiveAnalytics\data.csv')

"""
run this block of code ONCE to fix the S&P500 column, change file path to replace data.csv and then comment back out
"""
#dataframe['S&P500'] = dataframe['S&P500'].apply(lambda x: float(x.split()[0].replace(',', '')))
#dataframe.astype({'S&P500': 'float64'}).dtypes
#dataframe.to_csv(r'C:\DataAnalytics\DataAnalytics\DescriptiveAnalytics\data.csv')

descriptiveStatistics(dataframe)
#visualization calls
#barChart(dataframe)
#showHist(dataframe)
#lineCharts(dataframe)
plot2Columns(dataframe)