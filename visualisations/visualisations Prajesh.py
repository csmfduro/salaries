import pandas as pd
import matplotlib.pyplot as plt

# Loads CSV file containing salary data
file_path = "Salaries_data/salaries.csv"

try:
    data = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"Error: File not found at '{file_path}'")
    exit()

# Clean up labels for better readability
experience_labels = {
    'EN': 'Entry',
    'MI': 'Mid',
    'SE': 'Senior',
    'EX': 'Executive'
}

employment_labels = {
    'FT': 'Full-time',
    'PT': 'Part-time',
    'FR': 'Freelancer',
    'CT': 'Contract'
}

# Apply readable labels
data['experience_level'] = data['experience_level'].map(experience_labels)
data['employment_type'] = data['employment_type'].map(employment_labels)


# Q1: Compares the entry-Level High Paying Jobs vs Senior/Exec Low Paying Jobs
def entry_vs_senior_comparison():
    # Calculate average salary per (experience_level, job_title) combination
    salary_by_role = data.groupby(['experience_level', 'job_title'])['salary_in_usd'].mean().reset_index()

    # Highest-paying entry-level roles
    top_entry = salary_by_role[salary_by_role['experience_level'] == 'Entry']
    top_entry = top_entry.sort_values(by='salary_in_usd', ascending=False).head(5)

    # Lowest-paying senior or executive roles
    low_senior = salary_by_role[salary_by_role['experience_level'].isin(['Senior', 'Executive'])]
    low_senior = low_senior.sort_values(by='salary_in_usd').head(5)

    # Plots the results side-by-side
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    axes[0].barh(top_entry['job_title'], top_entry['salary_in_usd'], color='green')
    axes[0].set_title("Top Paying Entry-Level Jobs")
    axes[0].set_xlabel("Average Salary (USD)")

    axes[1].barh(low_senior['job_title'], low_senior['salary_in_usd'], color='red')
    axes[1].set_title("Lowest Paying Senior/Exec Jobs")
    axes[1].set_xlabel("Average Salary (USD)")

    plt.tight_layout()
    plt.show()

# Q2: Compares freelancers and Full-Time workers and analyses the tasks

def freelancer_vs_fulltime():
    # Calculate average salary by employment type
    avg_salary_by_type = data.groupby('employment_type')['salary_in_usd'].mean().round(2).sort_values(ascending=False)

    # Plot the average salary comparison
    plt.figure(figsize=(8, 5))
    avg_salary_by_type.plot(kind='bar', color='skyblue')
    plt.title("Freelancer vs Full-Time Salary Comparison")
    plt.ylabel("Average Salary (USD)")
    plt.xlabel("Employment Type")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # If freelancers are paid more, it will show top paying freelance roles
    freelancers = data[data['employment_type'] == 'Freelancer']
    fulltimers = data[data['employment_type'] == 'Full-time']

    avg_freelancer_salary = freelancers['salary_in_usd'].mean()
    avg_fulltime_salary = fulltimers['salary_in_usd'].mean()

    print("\nAverage Freelancer Salary: ${:,.2f}".format(avg_freelancer_salary))
    print("Average Full-Time Salary: ${:,.2f}".format(avg_fulltime_salary))

    if avg_freelancer_salary > avg_fulltime_salary:
        print("\nFreelancers earn more. Top paying freelance tasks:")
        top_freelance_roles = freelancers.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False).head(5).round(2)
    else:
        print("\nFreelancers earn less. Common freelance tasks:")
        top_freelance_roles = freelancers['job_title'].value_counts().head(5)

    print(top_freelance_roles) #displays role data

# ------------------------------------------------------------------------------------------
# Main Menu Loop
# ------------------------------------------------------------------------------------------
def menu():
    while True:
        print("\n Salary Insights Menu")
        print("1. Entry-Level High Paying vs Senior-Level Low Paying Jobs")
        print("2. Freelancers vs Full-Time Salary Comparison")
        print("0. Exit")

        selection = input("Choose an option: ")

        if selection == "1":
            entry_vs_senior_comparison()
        elif selection == "2":
            freelancer_vs_fulltime()
        elif selection == "0":
            print("Goodbye and Thank You !")
            break
        else:
            print("Invalid input. Please try again.")

# Start the app
menu()
