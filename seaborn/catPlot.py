import seaborn as sns, numpy as np, pandas as pd
import matplotlib.pyplot as plt

# Read in data as a pandas dataframe
wbd = pd.read_csv('wbd.csv')

# Convert string type to datetime type
wbd['Per Task Time'] = pd.to_datetime(wbd['Per Task Time'], errors='coerce')

# Create data frame with same date
df = pd.DataFrame({'date1':pd.date_range('2020-09-24', periods=189)})
df['date1'] = pd.to_datetime('2020-09-24')

# Convert from calendar date to Task Time (s)
df['diff'] = wbd['Per Task Time'] - df['date1']
wbd['Task Time (s)'] = df['diff'].dt.total_seconds()
wbd['Task Time (s)'] = wbd['Task Time (s)'].div(60)


# wbd['Task Time (s)'] = wbd['Per Task Time'].values.astype(float)

# print(wbd['Task Time (s)'])
# print(df['date1'])
# print(wbd['Per Task Time'])

# Create an array with the colors you want to use
colors = [ "#4374B3", "#FF0B04"]
# Set your custom color palette
sns.set_palette(sns.color_palette(colors))

# Draw a nested barplot by participant group and task
g = sns.catplot(
    data=wbd, kind="bar",
    x="Task", y="Task Time (s)", hue="Group",
    capsize=.1, zorder=5, ci=68, height=6
)
g.despine(left=True)
# g.set_axis_labels("", "Body mass (g)")
g.legend.set_title("Average Times Per Task for Each Group")

# remove default legend and place matplot legend in upper right
g._legend.remove()
plt.legend(loc='upper left')

# render graph
plt.show()
