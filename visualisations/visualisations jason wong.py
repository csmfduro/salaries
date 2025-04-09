import matplotlib.pyplot as plt
import pandas as pd
csvFilePath = "salaries_data\\salaries.csv"
dataset = pd.read_csv(csvFilePath)

def q5():
    "5.	what is the difference in average salary between companies with 100% remote work and 0% remote work"

    remote = dataset[dataset["remote_ratio"] == 100] #collecting by 100% remote work
    notRemote = dataset[dataset["remote_ratio"] == 0] #collecting by 0% remote work
    remoteAverage = remote["salary_in_usd"].mean().round(2) # calculating average salary in USD for 100% remote work
    notRemoteAverage = notRemote["salary_in_usd"].mean().round(2) #calculating average salary in USD for 0% remote work
    difference = (notRemoteAverage-remoteAverage).round(2) #finding difference between the salaries

    percentage = ["100%", "0%", "difference"] #x axis bar labels
    values=[remoteAverage, notRemoteAverage, difference] #x axis bar values
    fig, ax = plt.subplots() #creation of the graph
    ax.set_title("Difference in salary between 100% and 0% remote work", fontweight='bold') #title of graph
    ax.set_xlabel("Remote Work" , color='g') #x axis label coloured green
    ax.set_ylabel("Average Salary in USD", color='r') #y axis label coloured red
    ax.bar(percentage, values, zorder=3) #inputing the labels and values into the graph
    for i in range(len(percentage)):
        plt.text(i, values[i], values[i], ha="center", va="bottom" ) #displays values above bars
    ax.grid(zorder=0) #added grid lines to help understand values
    plt.tight_layout() 
    plt.show() #diplaying graph

def q6():
    "6.	what is the difference between the average salary in lockdown (2020) compared to this year (2025)"

    lockdown= dataset[dataset["work_year"] == 2020] #collecting by work year 2020
    recent= dataset[dataset["work_year"] == 2025] #collecting by work year 2025
    lockdownAverage = lockdown["salary_in_usd"].mean().round(2) #calculating average salary in USD for work year 2020
    recentAverage = recent["salary_in_usd"].mean().round(2) #calculating average salary in USD for work year 2025
    difference = (recentAverage-lockdownAverage).round(2) #finding difference between the salaries

    year = ["Lockdown (2020)", "Recent (2025)", "difference"] #x axis bar labels
    values=[lockdownAverage, recentAverage, difference] #x axis bar values
    fig, ax = plt.subplots() #creation of graph
    ax.set_title("Difference in salary between Lockdown (2020) and Recently (2025)", fontweight='bold') #title of graph
    ax.set_xlabel("Year/Time period" , color='g') #x axis label coloured green
    ax.set_ylabel("Average Salary in USD", color='r') #y axis label coloured red
    ax.bar(year, values, zorder=3) #inputing the labels and values into the graph
    for i in range(len(year)):
        plt.text(i, values[i], values[i], ha="center", va="bottom" ) #displays values above bars
    ax.grid(zorder=0) #added grid lines to help understand values
    plt.tight_layout()
    plt.show() #diplaying graph


while True:
        print("Questions:")
        print("5. what is the difference in average salary between companies with 100% remote work and 0% remote work")
        print("6. what is the difference between the average salary in lockdown (2020) compared to this year (2025)")
        print("0. Exit")
        #displaying options

        choice = input("\nEnter your choice: ") #taking user input for options
        
        match choice:
            case "5":
                q5() #displaying 5th question visualisation by calling its function
            case "6":
                q6() #displaying 6th question visualisation by calling its function
            case "0":
                print("Exiting the program.") #exiting program
                break
            case _:
                 print("Invalid option. Try again.") #validation incase unexpected inputs