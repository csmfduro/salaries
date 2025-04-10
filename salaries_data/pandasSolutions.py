import fileReader
import matplotlib.pyplot as plt

def q1():
  """ 1.	Which countries offer the highest salaries for AI professionals?
  Analyzes the dataset to identify the top 5 countries offering the highest average AI salaries. 
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
  top_countries = average_country_salary.sort_values(ascending=False).head(5).round(2)
  
  # Format the Dataframe to make it look nicer
  formatted_data = top_countries.reset_index()
  formatted_data.columns = ['Country Code', 'Average Salary (USD)']
  
  # Print only the top 5
  print("\n---------Top 5 Countries by Average AI Salary----------\n")
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
  
  def q9():
    """
    9. How do salaries differ between employees with and without a degree?
    Compares the average salary of employees who hold a degree versus those who do not.
    """
    df = fileReader.dataset

    # Clean/standardize education levels if necessary
    degree_levels = ['Bachelor’s', 'Master’s', 'PhD']
    df['has_degree'] = df['education_level'].isin(degree_levels)

    # Group by whether they have a degree or not
    salary_by_degree = df.groupby('has_degree')['salary_in_usd'].mean().round(2)

    print("\n--- Salary Comparison: With vs Without Degree ---\n")
    print(f"With Degree: ${salary_by_degree[True]}")
    print(f"Without Degree: ${salary_by_degree[False]}")
    print(f"Difference: ${(salary_by_degree[True] - salary_by_degree[False]).round(2)}")


def q10():
    """
    10. Is there a correlation between years of experience and salary?
    Calculates the correlation coefficient between years of experience and salary.
    """
    df = fileReader.dataset

    # Check for presence of experience-related column
    if 'years_of_experience' not in df.columns:
        print("Column 'years_of_experience' not found in the dataset.")
        return

    # Drop missing or non-numeric values
    df_clean = df[['years_of_experience', 'salary_in_usd']].dropna()

    # Calculate correlation
    correlation = df_clean['years_of_experience'].corr(df_clean['salary_in_usd'])

    print("\n--- Correlation between Years of Experience and Salary ---\n")
    print(f"Correlation coefficient: {correlation:.2f}")

    # Optional: give interpretation
    if correlation > 0.5:
        print("Strong positive correlation: More experience tends to result in higher salary.")
    elif correlation > 0.2:
        print("Moderate positive correlation.")
    elif correlation > 0:
        print("Weak positive correlation.")
    elif correlation == 0:
        print("No correlation.")
    else:
        print("Negative correlation: More experience may be linked to lower salaries (unusual case).")


def q11():
    """
    11. What is the average salary difference between the small, medium, and large companies?
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
    
    #Difference of highest and lowest average salary
    diff = (avg_salary_by_size.max() - avg_salary_by_size.min()).round(2)
    print(f"\nDifference between highest and lowest: ${diff}")


def q12():
  """
  12. Which countries offer the most remote opportunities?
  Identifies the top 5 company locations offering the highest number of 100% remote jobs.
  """
  df = fileReader.dataset  #Load dataset

  #Filter the dataset for 100% remote jobs
  remote_jobs = df[df["remote_ratio"] == 100]

  #Count the number of remote jobs by company location
  remote_counts = remote_jobs["company_location"].value_counts().head(5)

  #Format results for easier display
  formatted_data = remote_counts.reset_index()
  formatted_data.columns = ['Company Location', 'Number of Remote Jobs']

  #Display the top 5 results
  print("\n--- Top 5 Company Locations with the Most Remote Opportunities ---\n")
  print(formatted_data.to_string(index=False))





