# TODO: Read in CSVs, filter items by year, add on each column to existing dataframe
# WKDIR: C:\Users\raghu\Documents\Education\College\8 23 Spring Sem\CAP4784\Project\Datasets
# INVEST INTELLIGENCE

import pandas as pd
import numpy as np
import glob
from pathlib import Path

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
    
    elif fname == r'C:\DataAnalytics\DataAnalytics\DatasetCleaningTemp\Datasets\NASDAQCOM.csv':
      file = pd.read_csv(fname)
      file = NASDAQ_Cleaning(file)
      file.drop('DATE', inplace=True, axis=1)

      #print(file.iloc[:,0].values)
      #df["NASDAQ"] = file.iloc[:,0].values  #TODO does not like when I try to append nasdaq same way I did S&P above
      #TODO nasdaq has lest datapoints than it is supposed to must investigate
    
    else:
      file = pd.read_csv(fname)
      file.drop('DATE', inplace=True, axis=1)
      name = Path(fname).name
      name = str.removesuffix(name, '.csv')
      df[name] = file
  
  return df

def NASDAQ_Cleaning(dataSet):
  for index, row in dataSet.iterrows():
       
      if('01/01' not in row['DATE'] and '04/01' not in row['DATE'] 
         and '07/01' not in row['DATE'] and '12/01' not in row['DATE']):
          
          dataSet = dataSet.drop(labels=index, axis=0)
      
  return dataSet


def SPY_Cleaning(dataSet):
    for index, row in dataSet.iterrows():
       
      if('01/01' not in row['Date'] and '04/01' not in row['Date'] 
         and '07/01' not in row['Date'] and '12/01' not in row['Date']):
          
          dataSet = dataSet.drop(labels=index, axis=0)
      
    return dataSet

dataframe = pd.read_csv(r'C:\DataAnalytics\DataAnalytics\DatasetCleaningTemp\Datasets\CPI.csv')

dataframe = addingToDataFrame(dataframe)
dataframe = dataframe.set_index('DATE')
#print(dataframe)