import seaborn as sns, numpy as np, pandas as pd
import matplotlib.pyplot as plt

wbd = pd.read_csv('wbd_ft.csv')

# Convert string type to datetime type
wbd['Cumulative Time'] = pd.to_datetime(wbd['Cumulative Time'], errors='coerce')

# Create data frame with same date
df = pd.DataFrame({'date1':pd.date_range('2020-09-21', periods=21)})
df['date1'] = pd.to_datetime('2020-09-21')

# Convert from calendar date to Study Completion Time (s)
df['diff'] = wbd['Cumulative Time'] - df['date1']
wbd['Study Completion Time (s)'] = df['diff'].dt.total_seconds()
wbd['Study Completion Time (s)'] = wbd['Study Completion Time (s)'].div(60)

sns.kdeplot(data=wbd, x="Study Completion Time (s)", hue="Group", kind="kde")

plt.show()