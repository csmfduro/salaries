import matplotlib.pyplot as plt
import pandas as pd
csvFilePath = "Salaries Data\\salaries.csv"

def q5():
    "5.	what is the difference in average salary between companies with 100% remote work and 0% remote work"

    dataset = pd.read_csv(csvFilePath)

    remote = dataset[dataset["remote_ratio"] == 100] #collecting by 100% remote work
    notRemote = dataset[dataset["remote_ratio"] == 0] #collecting by 0% remote work
    remoteAverage = remote["salary_in_usd"].mean().round(2) # calculating average salary in USD for 100% remote work
    notRemoteAverage = notRemote["salary_in_usd"].mean().round(2) #calculating average salary in USD for 0% remote work
    difference = (notRemoteAverage-remoteAverage).round(2) #finding difference between the salaries

    percentage = ["100%", "0%", "difference"]
    values=[remoteAverage, notRemoteAverage, difference]
    fig, ax = plt.subplots()
    ax.set_title("Difference in salary between 100% and 0% remote work", fontweight='bold')
    ax.set_xlabel("Remote Work" , color='g')
    ax.set_ylabel("Average Salary in USD", color='r')
    ax.bar(percentage, values)
    plt.tight_layout()
    plt.show()

def q6():
    "6.	what is the difference between the average salary in lockdown (2020) compared to this year (2025)"

    dataset = pd.read_csv(csvFilePath)

    lockdown= dataset[dataset["work_year"] == 2020] #collecting by work year 2020
    recent= dataset[dataset["work_year"] == 2025] #collecting by work year 2025
    lockdownAverage = lockdown["salary_in_usd"].mean().round(2) #calculating average salary in USD for work year 2020
    recentAverage = recent["salary_in_usd"].mean().round(2) #calculating average salary in USD for work year 2025
    difference = (recentAverage-lockdownAverage).round(2) #finding difference between the salaries

    percentage = ["Lockdown (2020)", "Recent (2025)", "difference"]
    values=[lockdownAverage, recentAverage, difference]
    fig, ax = plt.subplots()
    ax.set_title("Difference in salary between Lockdown (2020) and Recently (2025)", fontweight='bold')
    ax.set_xlabel("Year/Time period" , color='g')
    ax.set_ylabel("Average Salary in USD", color='r')
    ax.bar(percentage, values)
    plt.tight_layout()
    plt.show()


while True:
        print("Questions:")
        print("5. what is the difference in average salary between companies with 100% remote work and 0% remote work")
        print("6. what is the difference between the average salary in lockdown (2020) compared to this year (2025)")
        print("0. Exit")

        choice = input("\nEnter your choice: ")
        
        match choice:
            case "5":
                q5()
            case "6":
                q6()
            case "0":
                print("Exiting the program.")
                break
            case _:
                 print("Invalid option. Try again.")