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
        print("5. Pick questions")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            viewDataset()
        elif choice == "2":
            viewColumnNames()
        elif choice == "3":
            viewDatasetInfo()
        elif choice == "4":
            viewQuestions()
        elif choice == "5":
            questionChoice()                                                         
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Try again.")
main()