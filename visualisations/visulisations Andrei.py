#13.	What is the average salary difference between the small, medium and large companies?
#14.	What location of companies have the highest salary?
import pandas as pd
import matplotlib.pyplot as plt

csvFilePath = "Salaries_data\\salaries.csv"
df = pd.read_csv(csvFilePath)

def visualisationQ13():
  """
  13. What is the average salary difference between small, medium, and large companies?
  Visualizes the average overall salary grouped by company size ('S', 'M', 'L').
  """
  grouped_by_size = df.groupby("company_size")
  average_salary_by_size = grouped_by_size["salary_in_usd"].mean().round(2).sort_values(ascending=False)



  # Optional relabeling for readability
  size_labels = {'L': 'Large', 'M': 'Medium', 'S': 'Small'}
  average_salary_by_size.index = average_salary_by_size.index.map(size_labels)
  formatted_data = average_salary_by_size.reset_index()
  axes = average_salary_by_size.plot(kind='bar', color='darkorange', figsize=(8, 6), zorder=3)

  # Set plot title and labels
  axes.set_title("Average Salary by Company Size", fontweight='bold', fontsize=17, fontname='Times New Roman')
  axes.set_xlabel("Company Size", fontweight='bold', fontsize=12)
  axes.set_ylabel("Average Salary (USD)", fontweight='bold', fontsize=12)
  axes.set_xticklabels(axes.get_xticklabels(), rotation=0)
  ymin, ymax = plt.ylim()
  xmin, xmax = plt.xlim()
  plt.text((xmax+xmax*0.1), (ymax-ymax*0.15), formatted_data)
  axes.grid(zorder=0)
  plt.tight_layout()
  plt.show()


def visualisationQ14():
  """
  14. What location of companies have the highest salary?
  Visualizes the top 5 company locations by average overall salary.
  """

  grouped_by_location = df.groupby("company_location")
  average_salary_by_location = grouped_by_location["salary_in_usd"].mean().round(2)
  top_locations = average_salary_by_location.sort_values(ascending=False).head(5)
  formatted_data = top_locations.reset_index()
  axes = top_locations.plot(kind='bar', color='purple', figsize=(10, 6), zorder=3)
  # Set plot title and labels
  axes.set_title("Top 5 Company Locations by Average Salary (USD)", fontweight='bold', fontsize=17, fontname='Times New Roman')
  axes.set_xlabel("Company Location (Country Code)", fontweight='bold', fontsize=12)
  axes.set_ylabel("Average Salary (USD)", fontweight='bold', fontsize=1)
  axes.set_xticklabels(axes.get_xticklabels(), rotation=90)
  axes.grid(zorder=0)
  ymin, ymax = plt.ylim()
  xmin, xmax = plt.xlim()
  plt.text((xmax+xmax*0.1), (ymax-ymax*0.15), formatted_data)
  plt.tight_layout()
  plt.show()
while True:
    print("Questions:")
    print("13. What is the average salary difference between the small, medium and large companies?")
    print("14. What location of companies have the highest salary?")
    print("0. Exit")

    choice = input("\nEnter your choice: ")

    match choice:
        case "13":
            visualisationQ13()
        case "14":
            visualisationQ14()
        case "0":
            print("Exiting the program.")
            break
        case _:
            print("Invalid option. Try again.")
