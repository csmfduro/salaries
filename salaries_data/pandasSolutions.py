import fileReader

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
  
  # Format the Dataframe to make it look nicer
  formatted_data = top_countries.reset_index()
  formatted_data.columns = ['Country Code', 'Average Salary (USD)']
  
  # Print only the top 10
  print("\n---------Top 10 Countries by Average AI Salary----------\n")
  print(formatted_data.to_string(index=False))
  return top_countries

    
def q2():
  """
  2. What are the highest-paying AI job titles?
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
  
  # Format the Dataframe to make it look nicer
  formatted_data = highest_paying_jobs.reset_index()
  formatted_data.columns = ['Job Title', 'Average Salary (USD)']
  
  # Display the top 8 highest-paying job titles
  print(highest_paying_jobs)
  for i, row in formatted_data.iterrows():
    print(f"{i+1}. {row['Job Title']}: {row['Average Salary (USD)']}")
  return highest_paying_jobs


def q5():
  "5.	what is the difference in average salary between companies with 100% remote work and 0% remote work"

  dataset= fileReader.dataset 

  remote = dataset[dataset["remote_ratio"] == 100] #collecting by 100% remote work
  notRemote = dataset[dataset["remote_ratio"] == 0] #collecting by 0% remote work
  remoteAverage = remote["salary_in_usd"].mean().round(2) # calculating average salary in USD for 100% remote work
  notRemoteAverage = notRemote["salary_in_usd"].mean().round(2) #calculating average salary in USD for 0% remote work
  difference = (notRemoteAverage-remoteAverage).round(2) #finding difference between the salaries
  
  print("\n100% remote work: $",remoteAverage) 
  print("0% remote work: $",notRemoteAverage) #displaying results
  print("Difference: $",difference)

def q6():
  "6.	what is the difference between the average salary in lockdown (2020) compared to this year (2025)"

  dataset= fileReader.dataset

  lockdown= dataset[dataset["work_year"] == 2020] #collecting by work year 2020
  recent= dataset[dataset["work_year"] == 2025] #collecting by work year 2025
  lockdownAverage = lockdown["salary_in_usd"].mean().round(2) #calculating average salary in USD for work year 2020
  recentAverage = recent["salary_in_usd"].mean().round(2) #calculating average salary in USD for work year 2025
  difference = (recentAverage-lockdownAverage).round(2) #finding difference between the salaries
  
  print("\nLockdown (2020): $",lockdownAverage)
  print("Recent(2025): $",recentAverage) #displaying results
  print("Difference: $",difference)