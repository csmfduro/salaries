import pandas as pd
import matplotlib.pyplot as plt

# Load dataset from CSV file
csvFilePath = "Salaries_data\\salaries.csv"
df = pd.read_csv(csvFilePath)

def plot_salary_by_location():
    """
    Q9: How do salaries vary based on company location?
    """
    print("\nQ9: How do salaries vary based on company location?")

    # Drop rows with missing company location or salary
    df_cleaned = df.dropna(subset=["company_location", "salary_in_usd"])

    # Get top 10 locations by number of records
    top_locations = (
        df_cleaned["company_location"]
        .value_counts()
        .head(10)
        .index
    )
    df_top = df_cleaned[df_cleaned["company_location"].isin(top_locations)]

    # Calculate average salary per location
    avg_salary_by_location = (
        df_top.groupby("company_location")["salary_in_usd"]
        .mean()
        .sort_values(ascending=False)
        .round(2)
    )

    print("\n--- Average Salary by Top Company Locations ---")
    print(avg_salary_by_location)

    # Plotting
    plt.figure(figsize=(10, 5))
    avg_salary_by_location.plot(kind='bar', color='teal')
    plt.title("Average Salary by Company Location (Top 10)")
    plt.ylabel("Salary (USD)")
    plt.xlabel("Company Location")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_experience_vs_salary():
    """
    Q10: How does salary vary with experience level?
    """
    print("\nQ10: How does salary vary with experience level?")

    # Define readable labels and desired order
    level_mapping = {
        "EN": "Entry-level",
        "MI": "Mid-level",
        "SE": "Senior-level",
        "EX": "Executive"
    }
    ordered_levels = ["EN", "MI", "SE", "EX"]

    # Drop rows with missing data
    df_cleaned = df.dropna(subset=["experience_level", "salary_in_usd"])

    # Keep only known levels and apply readable labels
    df_cleaned = df_cleaned[df_cleaned["experience_level"].isin(ordered_levels)]
    df_cleaned["experience_label"] = df_cleaned["experience_level"].map(level_mapping)

    # Calculate average salary per experience level
    avg_salary_by_exp = (
        df_cleaned.groupby("experience_label")["salary_in_usd"]
        .mean()
        .reindex([level_mapping[code] for code in ordered_levels])
        .round(2)
    )

    print("\n--- Average Salary by Experience Level ---")
    print(avg_salary_by_exp)

    # Plotting
    plt.figure(figsize=(7, 4))
    avg_salary_by_exp.plot(kind='bar', color='purple')
    plt.title("Average Salary by Experience Level")
    plt.ylabel("Salary (USD)")
    plt.xlabel("Experience Level")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


# Menu system
def main():
    while True:
        print("\n=== Salary Analysis Menu ===")
        print("9. Q9 - Salary by Company Location")
        print("10. Q10 - Salary by Experience Level")
        print("0. Exit")
        choice = input("Choose a question to run (0, 9, 10): ")

        if choice == '9':
            plot_salary_by_location()
        elif choice == '10':
            plot_experience_vs_salary()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid input. Please enter 0, 9, or 10.")

# Run the menu
main()
