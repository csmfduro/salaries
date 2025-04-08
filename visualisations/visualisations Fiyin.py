import pandas as pd
import matplotlib.pyplot as plt

csvFilePath = "Salaries_data\\salaries.csv"
df = pd.read_csv(csvFilePath)

def visualisationQ1():
  grouped = df.groupby("employee_residence")
  average_country_salary = grouped["salary_in_usd"].mean()
  top_countries = average_country_salary.sort_values(ascending=False).head(10).round(2)

  axes = top_countries.plot(kind='bar', color='indigo', figsize=(10, 6))
  # Set plot title and labels
  axes.set_title("Top 10 Countries by Average AI Salary (USD)", fontweight='bold', fontsize=17, fontname='Times New Roman')
  axes.set_xlabel("Country Code" , fontweight='bold', fontsize=12)
  axes.set_ylabel("Average Salary (USD)", fontweight='bold', fontsize=12)
  # Rotate X-axis labels for better readability
  axes.set_xticklabels(axes.get_xticklabels(), rotation=90)
  # Ensure everything fits inside the plot
  plt.tight_layout()
  plt.show()
  
def visualisationQ2():
  grouped_by_job = df.groupby("job_title")
  
  # Calculate the average salary in USD for each job title
  average_salary_by_job = grouped_by_job["salary_in_usd"].mean()
  
  # Sort the job titles by the highest average salary
  highest_paying_jobs = average_salary_by_job.sort_values(ascending=False)
  
  highest_paying_jobs =  highest_paying_jobs.head(8).round(2)
  
  plt.figure(figsize=(10, 6))
  highest_paying_jobs.plot(kind='bar', color='indigo')
  # Set plot title and labels
  plt.title("Top 8 Highest Paying Job Titles", fontweight='bold', fontsize=17, fontname='Times New Roman')
  plt.xlabel("Job Title", fontsize=13)
  plt.ylabel("Average Salary (USD)", fontsize=13)
  # Rotate X-axis labels for better readability
  plt.xticks(rotation=45, ha='right', fontsize= 9)
  plt.yticks(fontsize= 8)
  # Ensure everything fits inside the plot
  plt.tight_layout()
  plt.show()
  
while True:
        print("Questions:")
        print("1.	Which countries offer the highest salaries for AI professionals?")
        print("2.	What are the highest-paying AI job titles?")
        print("0. Exit")

        choice = input("\nEnter your choice: ")
        
        match choice:
            case "1":
                visualisationQ1()
            case "2":
                visualisationQ2()
            case "0":
                print("Exiting the program.")
                break
            case _:
                 print("Invalid option. Try again.")