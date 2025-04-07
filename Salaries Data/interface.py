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

# View the question and accept user input
def viewQuestions():
    for question in questions:
        print(question.strip())

    while True:
        try:
            num = int(input("Enter the your question number: "))
            if 1 <= num <= len(questions):
                print(f"\n{questions[num].strip()}")
                break  # Exit the loop once valid input is given
            else:
                print("Invalid number. Please enter a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
def main():
    while True:
        print("\nOptions:")
        print("1. View Dataset")
        print("2. View Column Names")
        print("3. View Dataset Info")
        print("4. View questions")
        print("5. Exit")

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
                print("Exiting the program.")
                break
            case _:
                 print("Invalid option. Try again.")
           
main()