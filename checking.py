import matplotlib.pyplot as plt
import numpy as np
from votes import wide as df
import seaborn as sns

sns.set()
plt.figure()

ax = sns.barplot(data=df, x="year", y="seats", hue="party", palette=['blue', 'red', 'yellow', 'grey'], saturation=0.6)

ax.set_title('UK election results')
ax.grid(color='#cccccc')
ax.set_ylabel('Seats')
ax.set_xlabel(None)
ax.set_xticklabels(df["year"].unique().astype(str), rotation='vertical')

plt.show()

print()