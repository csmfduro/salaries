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
  
  # Group the countries based on their salaries
  group_country_salary = grouped["salary_in_usd"]
  
  # Calculate the average salary
  average_country_salary = group_country_salary.mean()
  # Sort countries by highest average salary
  top_countries = average_country_salary.sort_values(ascending=False).head(10).round(2)
  
  # Format the Dataframe to make it look nicer
  formatted_data = top_countries.reset_index()
  formatted_data.columns = ['Country Code', 'Average Salary (USD)']
  
  # Print only the top 10
  print("\n---------Top 10 Countries by Average AI Salary----------\n")
  print(formatted_data.to_string(index=False))

    
def q2():
  """
  2. What are the highest-paying AI job titles?
  Analyzes the dataset to identify the highest-paying AI job titles by calculating the average salary for each title.
  The results are sorted by average salary in USD and the top 5 titles are displayed.
  
  """
  df = fileReader.dataset
  # Group by job_title
  grouped_by_job = df.groupby("job_title")
  
  # Calculate the average salary in USD for each job title
  average_salary_by_job = grouped_by_job["salary_in_usd"].mean()
  
  # Sort the job titles by the highest average salary
  highest_paying_jobs = average_salary_by_job.sort_values(ascending=False)
  
  highest_paying_jobs =  highest_paying_jobs.head(5).round(2)
  
  # Format the Dataframe to make it look nicer
  formatted_data = highest_paying_jobs.reset_index()
  formatted_data.columns = ['Job Title', 'Average Salary (USD)']
  
  # Display the top 8 highest-paying job titles
  print("\n")
  for i, row in formatted_data.iterrows():
    print(f"{i+1}. {row['Job Title']}: ${row['Average Salary (USD)']:.2f}")



def q3():
    """
    3. How much would an Entry Level/Junior of a high paying job make 
    compared to a low paying job but at Senior level or Executive level?
    """

    dataset = fileReader.dataset

    # Calculate average salary per job title
    job_averages = dataset.groupby("job_title")["salary_in_usd"].mean()

    # Identify highest and lowest paying job titles
    highestPayingJobTitle = job_averages.idxmax()
    lowestPayingJobTitle = job_averages.idxmin()

    # Filter dataset for those job titles
    highPayingJob = dataset[dataset["job_title"] == highestPayingJobTitle]
    lowPayingJob = dataset[dataset["job_title"] == lowestPayingJobTitle]

    # Filter by experience levels
    entryLevelHigh = highPayingJob[highPayingJob["experience_level"] == "EN"]
    seniorLow = lowPayingJob[lowPayingJob["experience_level"].isin(["SE", "EX"])]

    # Check for available data
    if entryLevelHigh.empty or seniorLow.empty:
        print("Not enough data for experience levels in selected jobs.")
        return

    # Calculate averages
    entryLevelHighAvg = entryLevelHigh["salary_in_usd"].mean().round(2)
    seniorLowAvg = seniorLow["salary_in_usd"].mean().round(2)
    difference = (entryLevelHighAvg - seniorLowAvg).round(2)

    # Display results
    print(f"\nEntry/Junior in highest-paying job ({highestPayingJobTitle}): ${entryLevelHighAvg}")
    print(f"Senior/Executive in lowest-paying job ({lowestPayingJobTitle}): ${seniorLowAvg}")
    print("Difference: $", difference)


def q4():
    """
    4. Do freelancers make more money or less money compared to full-time employees?
    If so, what freelance job/task pays well and if not, what jobs are freelancers doing?
    """

    dataset = fileReader.dataset

    # It filters by employment type
    freelancers = dataset[dataset["employment_type"] == "FL"]
    fullTime = dataset[dataset["employment_type"] == "FT"]

    # It calculates average salaries
    freelanceAvg = freelancers["salary_in_usd"].mean().round(2)
    fullTimeAvg = fullTime["salary_in_usd"].mean().round(2)

    # Finds the difference
    difference = (freelanceAvg - fullTimeAvg).round(2)

    # Finds the top freelance job and searches the most common freelance job
    topFreelanceJob = freelancers.groupby("job_title")["salary_in_usd"].mean().idxmax()
    topFreelancePay = freelancers.groupby("job_title")["salary_in_usd"].mean().max().round(2)

    commonFreelanceJob = freelancers["job_title"].mode()[0]

    print("\nFreelancers average salary: $", freelanceAvg)
    print("Full-time average salary: $", fullTimeAvg)
    print("Difference: $", difference)
    print("Highest paid freelance job:", topFreelanceJob, "with $", topFreelancePay)
    print("Most common freelance job:", commonFreelanceJob)


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


def q7():
  "7. What are the job titles for the lowest ten paying jobs (in ascending order)?"

  df = fileReader.dataset
  # Will be grouped by salary
  
  
  
  job_salary = df.groupby("job_title")["salary_in_usd"].mean()
  
  # Sort job titles by their respective salary
  low_title = job_salary.sort_values(ascending=True).head(10)
  
  # Format the Dataframe to make it look nicer
  formatted_data = low_title.reset_index()
  formatted_data.columns = ['\nJob Title', 'Average Salary (USD)\n']
  
  # Print only the top 10
  print("\n-10 lowest paying jobs and their titles-\n")
  print(formatted_data.to_string(index=False))
  return low_title


def q8():
  "8. What is the main trend between experience level and salary?"
  df = fileReader.dataset

  avg_salary_experience = df.groupby('experience_level')['salary_in_usd'].mean().round(2)
  print(avg_salary_experience)

  # Plotting the average salary by Experience Level
  avg_salary_exp.plot(kind='bar',)

  # Labels for Graph
  plt.title('Relationship between Experience level and Average Salary')
  plt.xlabel('Experience Level')
  plt.ylabel('Average Salary')

  plt.show()

def q13():
    """
    13. What is the average salary difference between the small, medium, and large companies?
    Groups the dataset by company size ('S', 'M', 'L') and calculates average salaries.
    """
    df = fileReader.dataset

    avg_salary_by_size = df.groupby("company_size")["salary_in_usd"].mean().round(2).sort_values(ascending=False)

    size_labels = {
        'L': 'Large',
        'M': 'Medium',
        'S': 'Small'
    }

    print("\n--- Average Salary by Company Size ---\n")
    for size, avg_salary in avg_salary_by_size.items():
        print(f"{size_labels.get(size, size)} Company: ${avg_salary}")
    
    # Optionally, show the difference between highest and lowest
    diff = (avg_salary_by_size.max() - avg_salary_by_size.min()).round(2)
    print(f"\nDifference between highest and lowest: ${diff}")


def q14():
  """
  14. What location of companies have the highest salary?
  Displays the top 5 company locations with the highest average overall salaries.
  """
  df = fileReader.dataset
  
  # Group by company location and calculate the average salary
  grouped_by_location = df.groupby("company_location")
  average_salary_by_location = grouped_by_location["salary_in_usd"].mean().round(2)
  
  # Get the top 5 locations with the highest average salary
  top_locations = average_salary_by_location.sort_values(ascending=False).head(5)
  
  # Format the DataFrame for cleaner output
  formatted_data = top_locations.reset_index()
  formatted_data.columns = ['Company Location', 'Average Salary (USD)']
  
  print("\n------Top 5 Company Locations by Average Salary------\n")
  print(formatted_data.to_string(index=False))






