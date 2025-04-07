import csv
import pandas as pd
#file name set allowing easy access if file ever is lost
csvFilePath = "Salaries Data\\salaries.csv"
questionsFilePath = "Salaries Data\\Questions.txt"
datasetInfo = "Salaries Data\\About_Salaries.txt"

def read(filePath, questionsFilePath, datasetInfo):
# Reads csv file
    dataset = pd.read_csv(filePath)
# Reads the questions
    with open(questionsFilePath, 'r') as file:
        questions = file.readlines()
# Reads the Dataset info
    with open(datasetInfo, 'r') as file:
        datasetInfo = file.readlines()
# Returns everything
    return dataset, questions, datasetInfo

dataset, questions, datasetInfo = read(csvFilePath, questionsFilePath, datasetInfo)