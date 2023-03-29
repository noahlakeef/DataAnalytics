# TODO: Read in CSVs, filter items by year, add on each column to existing dataframe
# WKDIR: C:\Users\raghu\Documents\Education\College\8 23 Spring Sem\CAP4784\Project\Datasets
# INVEST INTELLIGENCE

import pandas as pd
import numpy as np
import glob
from pathlib import Path

def addingToDataFrame(df):
  path = r'C:\Users\noahl\OneDrive\Desktop\Data Analytics\DatasetCleaningTemp\Datasets\*.csv'

  for fname in glob.glob(path): 

    if fname == r'C:\Users\noahl\OneDrive\Desktop\Data Analytics\DatasetCleaningTemp\Datasets\CPI.csv':
       continue
    
    elif fname == r'C:\Users\noahl\OneDrive\Desktop\Data Analytics\DatasetCleaningTemp\Datasets\S&P 500 Historical Data.csv':
      file = pd.read_csv(fname)
      
      file.drop('Open', inplace=True, axis=1)
      file.drop('High', inplace=True, axis=1)
      file.drop('Low', inplace=True, axis=1)
      file.drop('Vol.', inplace=True, axis=1)
      file.drop('Change %', inplace=True, axis=1)
      
      file = SPY_Cleaning(file)

      file.drop('Date', inplace=True, axis=1)
      #print(file)
      df["S&P500"] = file.iloc[:,0].values
      print(df)
      
    else:
      file = pd.read_csv(fname)
      file.drop('DATE', inplace=True, axis=1)
      name = Path(fname).name
      name = str.removesuffix(name, '.csv')
      df[name] = file
  
  return df

def NASDAQ_Cleaning():
  print('clean nasdaq dataset')
  # by cleaning this just means making the data quarterly and not daily


def SPY_Cleaning(dataSet):
    for index, row in dataSet.iterrows():
       
      if('01/01' not in row['Date'] and '04/01' not in row['Date'] 
         and '07/01' not in row['Date'] and '12/01' not in row['Date']):
          
          dataSet = dataSet.drop(labels=index, axis=0)
      
    return dataSet

#fedfunds = pd.read_csv(r'C:\Users\raghu\Documents\Education\College\8 23 Spring Sem\CAP4784\Project\Datasets\FEDFUNDS.csv')
#print(fedfunds)

dataframe = pd.read_csv(r'C:\Users\noahl\OneDrive\Desktop\Data Analytics\DatasetCleaningTemp\Datasets\CPI.csv')

dataframe = addingToDataFrame(dataframe)
dataframe = dataframe.set_index('DATE')
#print(dataframe)