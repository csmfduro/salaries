import pandas as pd
#file name set allowing easy access if file ever is lost
csvFilePath = "Salaries Data\\salaries.csv"
questionsFilePath = "Salaries Data\\Questions.txt"
datasetInfoFilePath = "Salaries Data\\About_Salaries.txt"

def read(csvFilePath, questionsFilePath, datasetInfoFilePath):
# Reads csv file
    dataset = pd.read_csv(csvFilePath)
# Reads the questions
    with open(questionsFilePath, 'r') as file:
        questions = file.readlines()
# Reads the Dataset info
    with open(datasetInfoFilePath, 'r') as file:
        datasetInfo = file.read()
# Returns everything
    return dataset, questions, datasetInfo

dataset, questions, datasetInfo = read(csvFilePath, questionsFilePath, datasetInfoFilePath)