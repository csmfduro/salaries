import csv
import pandas as pd
# Imports the contents of "fileReader.py"
import fileReader 

dataset = fileReader.dataset
questions = fileReader.questions
datasetInfo = fileReader.datasetInfo

def viewDataset():
    print("Viewing dataset.")
    print(dataset)

def viewColumnNames():
    print("Viewing column names.")
    columns = dataset.columns.values.tolist()
    print(columns)


def viewDatasetInfo():
    print("Viewing dataset info.")
    # with open(datasetInfo) as file:
    #     while line := file.readline():
    print(datasetInfo)

def viewQuestions():
    print(questions)
    
def questionChoice():
    print("Enter the question number")
    
def main():
    while True:
        print("\nOptions:")
        print("1. View Dataset")
        print("2. View Column Names")
        print("3. View Dataset Info")
        print("4. View questions")
        print("5. Pick question")
        print("6. Exit")

        choice = input("Enter your choice: ")
        
        match choice:
            case "1":
                viewDataset()
            case "2":
                viewColumnNames()
            case "3":
                viewDatasetInfo()
            case "4":
                viewQuestions()
            case "5":
                questionChoice()
            case "6":
                print("Exiting the program.")
                break
            case _:
                 print("Invalid option. Try again.")
           
main()