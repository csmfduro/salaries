import fileReader
import matplotlib.pyplot as plt

def q1():
  """ 1.	Which countries offer the highest salaries for AI professionals?
  Analyzes the dataset to identify the top 10 countries offering the highest average AI salaries. 
  The data is grouped by 'employee_residence' and sorted by average salary in USD.
  """
  df =  fileReader.dataset
  # Grouped by employee_residence
  grouped = df.groupby("employee_residence")
  # Find the average salary of each country
  average_country_salary = grouped["salary_in_usd"].mean()
  # Sort countries by highest average salary
  top_countries = average_country_salary.sort_values(ascending=False).head(10).round(2)
  # Print only the top 10
  print(top_countries)
  
  # plotting the chart
  axes = top_countries.head(10).plot(kind='bar', color='indigo', figsize=(10, 6))
  # Set plot title and labels
  axes.set_title("Top 10 Countries by Average AI Salary (USD)", fontweight='bold', fontsize=17, fontname='Times New Roman')
  axes.set_xlabel("Country Code" , fontweight='bold', fontsize=12)
  axes.set_ylabel("Average Salary (USD)", fontweight='bold', fontsize=12)
  # Rotate X-axis labels for better readability
  axes.set_xticklabels(axes.get_xticklabels(), rotation=90)
  # Ensure everything fits inside the plot
  plt.tight_layout()
  plt.show()
    
def q2():
  
  """ 2. What are the highest-paying AI job titles?
  Analyzes the dataset to identify the highest-paying AI job titles by calculating the average salary for each title.
  The results are sorted by average salary in USD and the top 8 titles are displayed.
  """
  
  df = fileReader.dataset
  # Group by job_title
  grouped_by_job = df.groupby("job_title")
  # Calculate the average salary in USD for each job title
  average_salary_by_job = grouped_by_job["salary_in_usd"].mean()
  # Sort the job titles by the highest average salary
  highest_paying_jobs = average_salary_by_job.sort_values(ascending=False).head(8).round(2)
  # Display the top 8 highest-paying job titles
  print(highest_paying_jobs)

  # plotting the chart
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