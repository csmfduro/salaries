import csv
import pandas as pd
#file name set allowing easy access if file ever is lost
filePath = "Salaries Data\\salaries.csv"

def read(filePath):
    dataset = pd.read_csv(filePath)
    return dataset

dataset = read(filePath)