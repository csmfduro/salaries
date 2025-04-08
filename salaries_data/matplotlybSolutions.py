
import pandasSolutions
import matplotlib.pyplot as plt
import pandasSolutions

def visualisationQ1():
  top_countries = pandasSolutions.q1()
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
  
def visualisationQ2():
  highest_paying_jobs = pandasSolutions.q2()
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
  
if __name__ == "__main__":
    visualisationQ1()
    visualisationQ2()
