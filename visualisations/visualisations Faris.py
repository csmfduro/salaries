import pandas as pd
import matplotlib.pyplot as plt

# Load dataset from CSV file
csvFilePath = "Salaries_data\\salaries.csv"
df = pd.read_csv(csvFilePath)


def plot_salary_by_currency():
    """
    Q9: How do salaries in different currencies (USD, EUR, GBP) compare when converted into USD?
    """
    print("\nQ9: How do salaries in different currencies (USD, EUR, GBP) compare when converted into USD?")

    # Filter for only USD, EUR, GBP
    df_filtered = df[df["salary_currency"].isin(["USD", "EUR", "GBP"])]
    df_filtered = df_filtered.dropna(subset=["salary_currency", "salary_in_usd"])

    # Calculate average salary by currency
    avg_salary_by_currency = (
        df_filtered.groupby("salary_currency")["salary_in_usd"]
        .mean()
        .sort_values(ascending=False)
        .round(2)
    )

    print("\n--- Average Salary by Currency (Converted to USD) ---")
    print(avg_salary_by_currency)

    # Plotting
    plt.figure(figsize=(6, 4))
    avg_salary_by_currency.plot(kind='bar', color='darkorange')
    plt.title("Average Salary by Currency (Converted to USD)")
    plt.ylabel("Salary (USD)")
    plt.xlabel("Currency")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


def plot_salary_by_employment_type_and_title():
    """
    Q10: How does the salary differ between full-time employees and other employment types,
    like part-time or freelance roles, across different job titles?
    """
    print("\nQ10: How does the salary differ between full-time employees and other employment types, like part-time or freelance roles, across different job titles?")

    # Drop missing values
    df_cleaned = df.dropna(subset=["employment_type", "job_title", "salary_in_usd"])

    # Get top 5 common job titles for readability
    top_titles = df_cleaned["job_title"].value_counts().head(5).index
    df_filtered = df_cleaned[df_cleaned["job_title"].isin(top_titles)]

    # Calculate average salary grouped by employment type and job title
    avg_salary = (
        df_filtered.groupby(["job_title", "employment_type"])["salary_in_usd"]
        .mean()
        .round(2)
        .unstack()
    )

    print("\n--- Average Salary by Employment Type & Job Title ---")
    print(avg_salary)

    # Plotting
    avg_salary.plot(kind="bar", figsize=(12, 6), colormap="viridis")
    plt.title("Average Salary by Employment Type Across Job Titles")
    plt.ylabel("Salary (USD)")
    plt.xlabel("Job Title")
    plt.xticks(rotation=45)
    plt.legend(title="Employment Type")
    plt.tight_layout()
    plt.show()


# Menu system
def main():
    while True:
        print("\n=== Salary Analysis Menu ===")
        print("9. Q9 - Salary by Currency (Converted to USD)")
        print("10. Q10 - Salary by Employment Type & Job Title")
        print("0. Exit")
        choice = input("Choose a question to run (0, 9, 10): ")

        if choice == '9':
            plot_salary_by_currency()
        elif choice == '10':
            plot_salary_by_employment_type_and_title()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid input. Please enter 0, 9, or 10.")

# Run the menu
main()
