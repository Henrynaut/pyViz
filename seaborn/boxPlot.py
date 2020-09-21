import seaborn as sns, numpy as np
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

ax = sns.boxplot(x="day", y="total_bill", hue="smoker",
                    data=tips, palette="Set3")
plt.show()