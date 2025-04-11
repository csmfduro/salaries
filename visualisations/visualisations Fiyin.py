import pandas as pd
import matplotlib.pyplot as plt

colors = ['teal', 'orange', 'purple', 'crimson', 'darkgreen']  # Different colors for the bars
csvFilePath = "Salaries_data\\salaries.csv"
df = pd.read_csv(csvFilePath)

def visualisationQ1():
  country_counts = df['employee_residence'].value_counts()
  filtered_countries = country_counts[country_counts > 10].index
  filtered_df = df[df['employee_residence'].isin(filtered_countries)]
  grouped_by_country = filtered_df.groupby("employee_residence")
  group_country_salary = grouped_by_country["salary_in_usd"]
  average_country_salary = group_country_salary.mean()
  top_countries = average_country_salary.sort_values(ascending=False).head(5).round(2)
  # Matplotlib
  fig, axes = plt.subplots(figsize=(12, 9))
  top_countries.plot(kind='bar', color=colors, zorder=3)
  # Set plot title and labels
  axes.set_title("Top 5 Countries by Average AI Salary (USD)", fontweight='bold', fontsize=17, fontname='Times New Roman')
  axes.set_xlabel("Country Code" , fontweight='bold', fontsize=12)
  axes.set_ylabel("Average Salary (USD)", fontweight='bold', fontsize=12)
  # Rotate X-axis labels for better readability
  axes.set_xticklabels(axes.get_xticklabels(), rotation=0)
    # Add a grid to the y axis
  axes.grid(axis='y', linestyle='--', zorder=0)
  # Made the values visible above the bars
  rects = axes.patches
  for rect in rects:
    height = rect.get_height() # Gets the height of the current bar
    bar_color = rect.get_facecolor() # Gets the color of the current bar
    x = rect.get_x() + rect.get_width() / 2 # Center of the bar
    axes.text(
    x, height + 8,  f"${height:,}",
    ha="center", va="bottom", fontsize=11, fontweight="bold", color =  bar_color )
  # Ensure everything fits inside the plot
  plt.tight_layout()
  plt.show()
  
def visualisationQ2():
  grouped_by_job = df.groupby("job_title")
  average_salary_by_job = grouped_by_job["salary_in_usd"].mean()
  highest_paying_jobs = average_salary_by_job.sort_values(ascending=False)
  highest_paying_jobs =  highest_paying_jobs.head(5).round(2).iloc[::-1]
  fig, axes = plt.subplots(figsize=(12, 8))
  highest_paying_jobs.plot(kind='barh', color=colors, zorder=2)
  # Set plot title and labels
  axes.set_title("Top 5 Highest Paying Job Titles", fontweight='bold', fontsize=17, fontname='Times New Roman')
  axes.set_ylabel("Job Title", fontsize=13, fontweight='bold')
  axes.set_xlabel("Average Salary (USD)", fontsize=13, fontweight='bold')
  # Add a grid to the x axis
  axes.grid(axis='x', linestyle='--', zorder=0)
  # Made the salaries appear inside the bar
  rects = axes.patches
  for rect in rects:
    width = rect.get_width()  # Length of the bar
    y = rect.get_y() + rect.get_height() / 2  # Center of the bar
    axes.text(
        (width/1.6) , y, f"${width:,.0f}",
        va='center', ha='right', fontsize=11, fontweight="bold", color='white'
    )
    
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