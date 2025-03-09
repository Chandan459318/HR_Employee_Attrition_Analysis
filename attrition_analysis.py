'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# ✅ Step 1: Connect to MySQL using SQLAlchemy
engine = create_engine("mysql+pymysql://root:root@127.0.0.1/hr_attrition")  # Replace 'your_password'

# ✅ Step 2: Load Data into Pandas DataFrame
query = "SELECT * FROM employee_attrition"
df = pd.read_sql(query, con=engine)

# ✅ Step 3: Display first few rows
print(df.head())

# ✅ Step 4: Check for Missing Values
print("Missing Values:\n", df.isnull().sum())

# ✅ Step 5: Check Data Types
print("\nData Types:\n", df.dtypes)



plt.figure(figsize=(6,4))
sns.countplot(x="attrition", data=df, hue="attrition", palette="coolwarm", legend=False)
plt.title("Overall Employee Attrition")
plt.show()



plt.figure(figsize=(10,5))

# Compute attrition rate by department
attrition_rate_by_dept = df[df["attrition"] == "Yes"].groupby("department")["attrition"].count() / df.groupby("department")["attrition"].count() * 100

# Reset index to make it plottable
attrition_rate_by_dept = attrition_rate_by_dept.reset_index()

# Create barplot
sns.barplot(x="department", y="attrition", data=attrition_rate_by_dept, palette="muted")

# Fix Title and Labels
plt.title("Attrition Rate by Department (%)")
plt.ylabel("Attrition Rate (%)")
plt.xlabel("Department")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x="attrition", y="monthly_income", data=df, palette="pastel")
plt.title("Monthly Income Distribution by Attrition")
plt.show()


plt.figure(figsize=(8,5))

# Compute attrition rate by work-life balance
attrition_rate_by_wlb = df[df["attrition"] == "Yes"].groupby("work_life_balance")["attrition"].count() / df.groupby("work_life_balance")["attrition"].count() * 100

# Reset index to make it plottable
attrition_rate_by_wlb = attrition_rate_by_wlb.reset_index()

# Create barplot
sns.barplot(x="work_life_balance", y="attrition", data=attrition_rate_by_wlb, palette="pastel")

# Fix Title and Labels
plt.title("Attrition Rate by Work-Life Balance (%)")
plt.ylabel("Attrition Rate (%)")
plt.xlabel("Work-Life Balance (1 = Poor, 4 = Excellent)")
plt.xticks(rotation=0)
plt.show()


plt.figure(figsize=(8,5))

# Compute attrition rate by overtime status
attrition_rate_by_overtime = df[df["attrition"] == "Yes"].groupby("overtime")["attrition"].count() / df.groupby("overtime")["attrition"].count() * 100

# Reset index to make it plottable
attrition_rate_by_overtime = attrition_rate_by_overtime.reset_index()

# Create barplot
sns.barplot(x="overtime", y="attrition", data=attrition_rate_by_overtime, palette="coolwarm")

# Fix Title and Labels
plt.title("Attrition Rate for Overtime Workers (%)")
plt.ylabel("Attrition Rate (%)")
plt.xlabel("Overtime (Yes = Works Overtime, No = Doesn't)")
plt.xticks(rotation=0)
plt.show()
'''
# HR Employee Attrition Analysis using Python & MySQL

# HR Employee Attrition Analysis using Python & MySQL

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# ✅ Step 1: Connect to MySQL using SQLAlchemy
try:
    engine = create_engine("mysql+pymysql://root:root@127.0.0.1/hr_attrition")  # Replace 'root' with your password if needed
    print("✅ Successfully connected to MySQL!")
except Exception as e:
    print("❌ Error connecting to MySQL:", e)
    exit()

# ✅ Step 2: Load Data into Pandas DataFrame
try:
    query = "SELECT * FROM employee_attrition"
    df = pd.read_sql(query, con=engine)
    print("✅ Data successfully loaded from MySQL!")
except Exception as e:
    print("❌ Error loading data:", e)
    exit()

# ✅ Step 3: Display first few rows
print("\n📊 First 5 rows of the dataset:\n", df.head())

# ✅ Step 4: Check for Missing Values
missing_values = df.isnull().sum()
print("\n❗ Missing Values:\n", missing_values)

# ✅ Step 5: Check Data Types
print("\n🔍 Data Types:\n", df.dtypes)

# ✅ Ensure 'years_at_company' is numeric before visualization
df["years_at_company"] = pd.to_numeric(df["years_at_company"], errors="coerce")

# 🎯 Step 6: Data Visualizations
sns.set_style("whitegrid")

# ✅ 1. Overall Employee Attrition Rate
plt.figure(figsize=(6, 4))
sns.countplot(x="attrition", data=df, palette=["#FF6F61", "#6B9AC4"])
plt.title("Overall Employee Attrition")
plt.xlabel("Attrition (Yes = Left, No = Stayed)")
plt.ylabel("Employee Count")
plt.show()

# ✅ 2. Attrition Rate by Department
plt.figure(figsize=(10, 5))
attrition_rate_by_dept = df[df["attrition"] == "Yes"].groupby("department")["attrition"].count() / df.groupby("department")["attrition"].count() * 100
attrition_rate_by_dept = attrition_rate_by_dept.reset_index()
sns.barplot(x="department", y="attrition", data=attrition_rate_by_dept, palette="muted")
plt.title("Attrition Rate by Department (%)")
plt.ylabel("Attrition Rate (%)")
plt.xlabel("Department")
plt.xticks(rotation=45)
plt.show()

# ✅ 3. Monthly Income Distribution by Attrition
plt.figure(figsize=(8, 5))
sns.boxplot(x="attrition", y="monthly_income", data=df, palette=["#FF6F61", "#6B9AC4"])
plt.title("Monthly Income Distribution by Attrition")
plt.xlabel("Attrition")
plt.ylabel("Monthly Income ($)")
plt.show()

# ✅ 4. Attrition by Work-Life Balance
plt.figure(figsize=(8, 5))
attrition_rate_by_wlb = df[df["attrition"] == "Yes"].groupby("work_life_balance")["attrition"].count() / df.groupby("work_life_balance")["attrition"].count() * 100
attrition_rate_by_wlb = attrition_rate_by_wlb.reset_index()
sns.barplot(x="work_life_balance", y="attrition", data=attrition_rate_by_wlb, palette="pastel")
plt.title("Attrition Rate by Work-Life Balance (%)")
plt.ylabel("Attrition Rate (%)")
plt.xlabel("Work-Life Balance (1 = Poor, 4 = Excellent)")
plt.show()

# ✅ 5. Impact of Overtime on Attrition
plt.figure(figsize=(8, 5))
attrition_rate_by_overtime = df[df["attrition"] == "Yes"].groupby("overtime")["attrition"].count() / df.groupby("overtime")["attrition"].count() * 100
attrition_rate_by_overtime = attrition_rate_by_overtime.reset_index()
sns.barplot(x="overtime", y="attrition", data=attrition_rate_by_overtime, palette="coolwarm")
plt.title("Attrition Rate for Overtime Workers (%)")
plt.ylabel("Attrition Rate (%)")
plt.xlabel("Overtime (Yes = Works Overtime, No = Doesn't)")
plt.show()

# ✅ 6. Attrition Rate by Age Group
plt.figure(figsize=(10, 5))
sns.histplot(df[df["attrition"] == "Yes"]["age"], bins=10, kde=True, color="red", label="Attrition")
sns.histplot(df[df["attrition"] == "No"]["age"], bins=10, kde=True, color="blue", label="No Attrition")
plt.title("Attrition Rate by Age Group")
plt.xlabel("Age")
plt.ylabel("Count")
plt.legend()
plt.show()

# ✅ 7. Attrition Rate by Years at Company
plt.figure(figsize=(10, 5))
attrition_rate_by_years = df[df["attrition"] == "Yes"].groupby("years_at_company")["attrition"].count() / df.groupby("years_at_company")["attrition"].count() * 100
attrition_rate_by_years = attrition_rate_by_years.reset_index()
sns.barplot(x="years_at_company", y="attrition", data=attrition_rate_by_years, palette="PuRd")
plt.title("Attrition Rate by Years at Company (%)")
plt.ylabel("Attrition Rate (%)")
plt.xlabel("Years at Company")
plt.xticks(rotation=0)
plt.show()


# ✅ 8. Attrition Rate by Job Satisfaction
import matplotlib.pyplot as plt
import seaborn as sns

# ✅ Precompute the attrition rate by job satisfaction
attrition_rate_by_js = df[df["attrition"] == "Yes"].groupby("job_satisfaction")["attrition"].count() / df.groupby("job_satisfaction")["attrition"].count() * 100
attrition_rate_by_js = attrition_rate_by_js.reset_index()

# ✅ Plot
plt.figure(figsize=(8, 5))
sns.barplot(x="job_satisfaction", y="attrition", data=attrition_rate_by_js, palette="Blues")

plt.title("Attrition Rate by Job Satisfaction (%)")
plt.ylabel("Attrition Rate (%)")
plt.xlabel("Job Satisfaction Level (1-4)")
plt.show()



# ✅ 9. Attrition Rate by Education Level
import matplotlib.pyplot as plt
import seaborn as sns

# ✅ Precompute the attrition rate by education level
attrition_rate_by_edu = df[df["attrition"] == "Yes"].groupby("education_level")["attrition"].count() / df.groupby("education_level")["attrition"].count() * 100
attrition_rate_by_edu = attrition_rate_by_edu.reset_index()

# ✅ Plot
plt.figure(figsize=(8, 5))
sns.barplot(x="education_level", y="attrition", data=attrition_rate_by_edu, palette="coolwarm")

plt.title("Attrition Rate by Education Level (%)")
plt.ylabel("Attrition Rate (%)")
plt.xlabel("Education Level (1 = Low, 5 = High)")
plt.xticks(rotation=45)  # Rotate labels if needed
plt.show()



# ✅ Export cleaned dataset to CSV
df.to_csv("HR_Employee_Attrition_Cleaned.csv", index=False)
print("\n✅ Data successfully exported to HR_Employee_Attrition_Cleaned.csv!")

