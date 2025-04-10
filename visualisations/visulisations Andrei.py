#11.	What is the average salary difference between the small, medium and large companies?
#12.	Which countries offer the most remote opportunities?
import pandas as pd
import matplotlib.pyplot as plt

csvFilePath = "Salaries_data\\salaries.csv"
df = pd.read_csv(csvFilePath)

def visualisationQ11():
  """
  11. What is the average salary difference between small, medium, and large companies?
  Visualizes the average overall salary grouped by company size ('S', 'M', 'L').
  """

  #Group the dataset by company size
  grouped_by_size = df.groupby("company_size")

  #Calculate the average salary for each company size and sort in descending order
  average_salary_by_size = grouped_by_size["salary_in_usd"].mean().round(2).sort_values(ascending=False)

  #Makes it readable
  size_labels = {'L': 'Large', 'M': 'Medium', 'S': 'Small'}
  average_salary_by_size.index = average_salary_by_size.index.map(size_labels)

  #Makes sure it looks nice and presentable
  formatted_data = average_salary_by_size.reset_index()

  #Bar chart
  axes = average_salary_by_size.plot(kind='bar', color='darkorange', figsize=(8, 6), zorder=3)

  #Set the title and axis labels
  axes.set_title("Average Salary by Company Size", fontweight='bold', fontsize=17, fontname='Times New Roman')
  axes.set_xlabel("Company Size", fontweight='bold', fontsize=12)
  axes.set_ylabel("Average Salary (USD)", fontweight='bold', fontsize=12)

  #Keeps the labels horizontaly so it is readable
  axes.set_xticklabels(axes.get_xticklabels(), rotation=0)

  #Add a text box in the right corner for readability
  ymin, ymax = plt.ylim()
  xmin, xmax = plt.xlim()
  plt.text((xmax + xmax * 0.1), (ymax - ymax * 0.15), formatted_data.to_string(index=False))

  #Adds grid lines
  axes.grid(zorder=0)

  #Fits the text I added and everything well together
  plt.tight_layout()
  plt.show()


def visualisationQ12():
  """
  12. Which countries offer the most remote opportunities?
  Visualizes the top 5 company locations with the highest number of 100% remote jobs.
  """

  #Filter for 100% remote roles
  remote_jobs = df[df["remote_ratio"] == 100]
  
  #Actual data
  remote_counts = remote_jobs["company_location"].value_counts().head(5)
  
  #This is to display data
  formatted_data = remote_counts.reset_index()
  formatted_data.columns = ['Company Location', 'Number of Remote Jobs']
  
  #Plot
  axes = remote_counts.plot(kind='bar', color='slateblue', figsize=(10, 6), zorder=3)

  #Set plot title and labels
  axes.set_title("Top 5 Company Locations with Most Remote Opportunities", fontweight='bold', fontsize=17, fontname='Times New Roman')
  axes.set_xlabel("Company Location (Country Code)", fontweight='bold', fontsize=12)
  axes.set_ylabel("Number of 100% Remote Jobs", fontweight='bold', fontsize=12)
  axes.set_xticklabels(axes.get_xticklabels(), rotation=90)
  axes.grid(zorder=0)

  #Text block which demonstrates the data raw which makes it easier to read
  ymin, ymax = plt.ylim()
  xmin, xmax = plt.xlim()
  plt.text((xmax + xmax * 0.1), (ymax - ymax * 0.15), formatted_data.to_string(index=False))

  #This ensures that the information that I add in the corner and the graph is neat
  plt.tight_layout()
  plt.show()
while True:
    print("Questions:")
    print("11. What is the average salary difference between the small, medium and large companies?")
    print("12. What location of companies have the highest salary?")
    print("0. Exit")

    choice = input("\nEnter your choice: ")

    match choice:
        case "11":
            visualisationQ11()
        case "12":
            visualisationQ12()
        case "0":
            print("Exiting the program.")
            break
        case _:
            print("Invalid option. Try again.")
