# WKDIR: C:\Users\raghu\Documents\Education\College\8 23 Spring Sem\CAP4784\Project\Datasets
# INVEST INTELLIGENCE

import pandas as pd
import numpy as np
import glob
from pathlib import Path

"""
THIS METHOD LOOPS THROUGH ALL THE CSVS, AND APPENDS THEM TO THE DATAFRAME.
IF THE CSV IS NASDAQ OR S&P500 IT CALLS THEIR RESPECTIVE CLEANING METHODS THEN APPENDS TO DATAFRAME
"""
def addingToDataFrame(df):
  path = r'C:\DataAnalytics\DataAnalytics\DatasetCleaningTemp\Datasets\*.csv'

  for fname in glob.glob(path): 

    #ignore CPI was loaded before func call
    if fname == r'C:\DataAnalytics\DataAnalytics\DatasetCleaningTemp\Datasets\CPI.csv':
       continue
    
    #read in and edit S&P500 
    elif fname == r'C:\DataAnalytics\DataAnalytics\DatasetCleaningTemp\Datasets\S&P 500 Historical Data.csv':
      file = pd.read_csv(fname)
      
      file.drop('Open', inplace=True, axis=1)
      file.drop('High', inplace=True, axis=1)
      file.drop('Low', inplace=True, axis=1)
      file.drop('Vol.', inplace=True, axis=1)
      file.drop('Change %', inplace=True, axis=1)
      
      file = SPY_Cleaning(file)

      file.drop('Date', inplace=True, axis=1)
      df["S&P500"] = file.iloc[:,0].values
      print(df)
    
    # reading in NASDAQ .csv
    elif fname == r'C:\DataAnalytics\DataAnalytics\DatasetCleaningTemp\Datasets\NASDAQCOM.csv':
      file = pd.read_csv(fname)
      file = NASDAQ_Cleaning(file)
      file.drop('DATE', inplace=True, axis=1) # drop DATE column
      
      df["NASDAQ"] = file.iloc[:,0].values  # appends nasdaq values to dataframe
    
    #reading in any other .csv
    else:
      file = pd.read_csv(fname)
      file.drop('DATE', inplace=True, axis=1)
      name = Path(fname).name
      name = str.removesuffix(name, '.csv')
      df[name] = file
  
  return df

"""
THIS METHOD CLEANS THE NASDAQ DATASET
"""
def NASDAQ_Cleaning(dataSet):

  i = 0
  #this loops through the dataset and finds any blank values and replaces them with the nearest non-blank value
  for index, row in dataSet.iterrows():
    if i == 0:
      prevRow = row
      i += 1
      continue

    if row['NASDAQCOM'] == '.':
      row['NASDAQCOM' ] = prevRow['NASDAQCOM']
    else:
      prevRow = row
    
  #this loops through the data set and removes and row that is not a quarterly date      
  for index, row in dataSet.iterrows():
       
      if('01/01' not in row['DATE'] and '04/01' not in row['DATE'] 
         and '07/01' not in row['DATE'] and '10/01' not in row['DATE']):
          
          dataSet = dataSet.drop(labels=index, axis=0)
  
  return dataSet

"""
THIS METHOD CLEANS THE S&P500 DATASET
"""
def SPY_Cleaning(dataSet):
    #this loops through the data set and removes and row that is not a quarterly date   
    for index, row in dataSet.iterrows():
      if('01/01' not in row['Date'] and '04/01' not in row['Date'] 
         and '07/01' not in row['Date'] and '10/01' not in row['Date']):
          
          dataSet = dataSet.drop(labels=index, axis=0)
      
    return dataSet

#we read in the CPI .csv first to create the dataset
dataframe = pd.read_csv(r'C:\DataAnalytics\DataAnalytics\DatasetCleaningTemp\Datasets\CPI.csv')
#then we call the function that controls the cleaning and appending to the dataframe
dataframe = addingToDataFrame(dataframe)
#this makes the index of the data frame the DATE
dataframe = dataframe.set_index('DATE')