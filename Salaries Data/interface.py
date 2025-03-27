def loadDataset():  
    print("Dataset loaded.")

def viewDataset():
    print("Viewing dataset.")

def viewColumnNames():
    print("Viewing column names.")

def viewDatasetInfo():
    print("Viewing dataset info.")

def questionChoice():
    print("Pick one of these questions.")

def main():
    while True:
        print("\nOptions:")
        print("1. Load Dataset")
        print("2. View Dataset")
        print("3. View Column Names")
        print("4. View Dataset Info")
        print("5. Pick a question")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            loadDataset()
        elif choice == "2":
            viewDataset()
        elif choice == "3":
            viewColumnNames()
        elif choice == "4":
            viewDatasetInfo()
        elif choice == "5":
            questionChoice()                                                          
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Try again.")
main()