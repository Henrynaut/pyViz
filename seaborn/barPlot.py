import seaborn as sns, numpy as np, pandas as pd
import matplotlib.pyplot as plt

# Read in data as a pandas dataframe
wbd = pd.read_csv('wbd.csv')

# Convert string type to datetime type
wbd['Per Task Time'] = pd.to_datetime(wbd['Per Task Time'], errors='coerce')

# Create data frame with same date
df = pd.DataFrame({'date1':pd.date_range('2020-09-23', periods=189)})
df['date1'] = pd.to_datetime('2020-09-23')

# Convert from calendar date to Task Time (s)
df['diff'] = wbd['Per Task Time'] - df['date1']
wbd['Task Time (s)'] = df['diff'].dt.total_seconds()
wbd['Task Time (s)'] = wbd['Task Time (s)'].div(60)


# wbd['Task Time (s)'] = wbd['Per Task Time'].values.astype(float)

# print(wbd['Task Time (s)'])
# print(df['date1'])
# print(wbd['Per Task Time'])


sns.barplot(x="Task", y="Task Time (s)", data=wbd, ci="sd") 
plt.show()
