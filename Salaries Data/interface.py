import csv
import pandas as pd

datasetInfo= "Salaries Data\\About_Salaries.txt"
filePath = "Salaries Data\\salaries.csv"

def read(filePath):
    dataset = pd.read_csv(filePath)
    print("dataset loaded")
    return dataset

dataset = read(filePath)

def viewDataset():
    print("Viewing dataset.")
    print(dataset)

def viewColumnNames():
    print("Viewing column names.")
    columns = dataset.columns.values.tolist()
    print(columns)


def viewDatasetInfo():
    print("Viewing dataset info.")
    with open(datasetInfo) as file:
        while line := file.readline():
            print(line.rstrip())

def questionChoice():
    print("Pick one of these questions.")

def main():
    while True:
        print("\nOptions:")
        print("1. View Dataset")
        print("2. View Column Names")
        print("3. View Dataset Info")
        print("4. Pick a question")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            viewDataset()
        elif choice == "2":
            viewColumnNames()
        elif choice == "3":
            viewDatasetInfo()
        elif choice == "4":
            questionChoice()                                                          
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Try again.")
main()