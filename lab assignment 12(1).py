import pandas as pd
import matplotlib.pyplot as plt

# Creating dummy dataset for recruitment
recruit_data = {
    'Company': ['Microsoft', 'Google', 'Amazon', 'IBM', 'Deloitte', 'Capgemini', 'ATOS Origin', 'Amdocs'],
    'New_Recruitments': [1500, 1800, 2200, 1200, 900, 1100, 600, 850]
}
df_recruit = pd.DataFrame(recruit_data)

# a) Bar Chart
plt.figure(figsize=(10, 5))
plt.bar(df_recruit['Company'], df_recruit['New_Recruitments'], color='teal')
plt.title('New Recruitments by Company')
plt.xticks(rotation=45)
plt.show()

# b) Pie Chart & c) Customized Pie Chart
plt.figure(figsize=(7, 7))
explode = [0.1 if x == 'Google' else 0 for x in df_recruit['Company']] # Highlight Google
plt.pie(df_recruit['New_Recruitments'], labels=df_recruit['Company'], autopct='%1.1f%%', explode=explode, shadow=True)
plt.title('Distribution of New Recruitments')
plt.show()

# d) Doughnut Chart
plt.figure(figsize=(7, 7))
plt.pie(df_recruit['New_Recruitments'], labels=df_recruit['Company'], autopct='%1.1f%%', pctdistance=0.85)
# Draw center circle to make it a doughnut
centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title('Recruitment Doughnut Chart')
plt.show()

# Comparison between IBM & Amdocs
compare_df = df_recruit[df_recruit['Company'].isin(['IBM', 'Amdocs'])]
plt.figure(figsize=(6, 4))
plt.bar(compare_df['Company'], compare_df['New_Recruitments'], color=['blue', 'orange'])
plt.title('Comparison: IBM vs Amdocs Recruitments')
plt.ylabel('Number of Employees')
plt.show()
