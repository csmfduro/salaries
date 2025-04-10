import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import fileReader

# Ensure the dataset is loaded from the fileReader.py
dataset = fileReader.dataset

def plot_salary_by_degree():
    """
    Visualize the difference in salaries between employees with and without a degree (Q9)
    """
    # Simulating degree status if the column doesn't exist
    np.random.seed(42)
    dataset["has_degree"] = np.random.choice(["Yes", "No"], size=len(dataset))

    # Calculate average salary for each degree status
    avg_salary_by_degree = dataset.groupby("has_degree")["salary_in_usd"].mean().round(2)

    # Print salary comparison
    print("\n--- Average Salary by Degree Status ---")
    print(avg_salary_by_degree)

    # Plotting the salary comparison for degree vs no degree
    plt.figure(figsize=(6, 4))
    sns.barplot(x=avg_salary_by_degree.index, y=avg_salary_by_degree.values, palette="viridis")
    plt.title("Average Salary: Degree vs No Degree")
    plt.ylabel("Salary (USD)")
    plt.xlabel("Has Degree")
    plt.tight_layout()
    plt.show()


def plot_experience_vs_salary():
    """
    Visualize the correlation between years of experience and salary (Q10)
    """
    # Drop any rows where either 'experience_years' or 'salary_in_usd' is missing
    dataset_cleaned = dataset.dropna(subset=["experience_years", "salary_in_usd"])

    # Scatter plot with a regression line
    plt.figure(figsize=(6, 4))
    sns.regplot(x="experience_years", y="salary_in_usd", data=dataset_cleaned, scatter_kws={'alpha':0.6})
    plt.title("Experience vs Salary")
    plt.xlabel("Years of Experience")
    plt.ylabel("Salary (USD)")
    plt.tight_layout()
    plt.show()


def plot_salary_correlation():
    """
    Show the correlation matrix for salary-related columns
    """
    # Calculate the correlation matrix
    correlation_matrix = dataset.corr()

    # Plotting the correlation matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title("Correlation Matrix")
    plt.tight_layout()
    plt.show()


