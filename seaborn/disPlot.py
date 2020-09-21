import seaborn as sns, numpy as np
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")
sns.displot(data=penguins, x="flipper_length_mm", kde=True)

plt.show()