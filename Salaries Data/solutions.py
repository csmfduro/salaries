"""1. Which countries offer the highest salaries for AI professionals? """

import pandas as pd
import fileReader
import matplotlib.pyplot as plt

def q1():
  df =  fileReader.dataset
  # Grouped by employee_residence
  grouped = df.groupby("employee_residence")
  # Find the average salary of each country
  average_country_salary = grouped["salary_in_usd"].mean()
  # Sort countries by highest average salary
  top_countries = average_country_salary.sort_values(ascending=False)
  top_countries = top_countries.head(10).round(2)
  # Print only the top 10
  print(top_countries)
  
  # plotting the chart
  ax = top_countries.head(10).plot(kind='bar', color='skyblue', figsize=(10, 6))
  # Set plot title and labels
  plt.title("Top 10 Countries by Average AI Salary (USD)")
  plt.xlabel("Country Code")
  plt.ylabel("Average Salary (USD)")
  # Rotate X-axis labels for better readability
  plt.xticks(rotation=45)
  # Ensure everything fits inside the plot
  plt.tight_layout()
  plt.show()
    
