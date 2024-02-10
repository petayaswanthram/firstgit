import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a Pandas DataFramepippip
df = pd.read_csv("students.csv")

# Create three separate DataFrames for each age group
df_below_20 = df[df['AGE'] < 20]
df_20_to_25 = df[(df['AGE'] >= 20) & (df['AGE'] <= 25)]
df_above_25 = df[df['AGE'] > 25]

# Calculate the average grade for each age group
avg_grade_below_70 = df_below_20['GRADE'].mean()
avg_grade_70_to_80 = df_20_to_25['GRADE'].mean()
avg_grade_above_80 = df_above_25['GRADE'].mean()

# Create a bar plot
age_groups = ['Below 20', '20-25', 'Above 25']
average_grades = [avg_grade_below_70, avg_grade_70_to_80, avg_grade_above_80]

plt.bar(age_groups, average_grades, color='skyblue')
plt.xlabel('Age Groups')
plt.ylabel('Average Grade')
plt.title('Average Grade for Different Age Groups')
plt.show()
