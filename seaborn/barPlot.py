import seaborn as sns, numpy as np
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.barplot(x="day", y="tip", data=tips, ci="sd") 
plt.show()
