import matplotlib.pyplot as plt
import pandas as pd
import fileReader

csvFilePath = "salaries_data\\salaries.csv"
dataset = pd.read_csv(csvFilePath)

def q7():
  "7. What are the job titles for the lowest ten paying jobs (in ascending order)?"

  df = dataset
  
  # Will be grouped by salary
  job_salary = df.groupby("job_title")["salary_in_usd"].mean()
  
  # Sort job titles by their respective salary
  low_title = job_salary.sort_values(ascending=True).head(10)
  
  # Format dataframe for clarity
  formatted_data = low_title.reset_index()
  formatted_data.columns = ['Job Title', 'Average Salary (USD)']
  
  # Print only the top 10
  print("-10 lowest paying jobs and their titles-")
  print(formatted_data.to_string(index=False))
  return low_title


def q8():
  "8. What is the main trend between experience level and salary?"
  df = dataset
  #Grouping the experience level by USD Salary
  avg_salary_exp = df.groupby('experience_level')['salary_in_usd'].mean()
  #Prints values to use in grahpical representation
  print(avg_salary_exp)

  #formatting the data for clarity
  formatted_data = avg_salary_exp.reset_index()
  # formatted_data.columns = ['Experience Level', 'Average Salary (USD)']
  axes = avg_salary_exp.plot(kind='bar', color='Blue', figsize=(10, 6), zorder=3)
  # Set plot title and labels
  axes.set_title("Average Salary Based on work Experience", fontweight='bold')
  axes.set_xlabel('experience_level'), 
  axes.set_ylabel('Average Salary (USD)'),
  #added grid for better visualisation
  axes.set_xticklabels(axes.get_xticklabels(), rotation=90)
  axes.grid(zorder=0)
  ymin, ymax = plt.ylim()
  xmin, xmax = plt.xlim()
  plt.tight_layout()
  plt.show()

# Interface 
while True:
        print("Questions:")
        print("7. What are the job titles for the lowest ten paying jobs (in ascending order)?")
        print("8. What is the main trend between experience level and salary?")
        print("0. Exit")

        choice = input("\nEnter your choice: ")
        #Choices / options for user to select
        match choice:
            case "7":
                q7()
            case "8":
                q8()
            case "0":
                print("Exiting the program.")
                break
            case _:
                 # Only allows 7,8,0 to be entered therefore negating any issues with other datatypes or inputs being used.
                 print("Invalid Try again.")


