import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

special = pd.read_csv("SpecializedData.csv")
special.dropna(how='all', inplace=True)
special = special.drop([5], axis = 0, )

special = special.plot(kind='bar', x='Specialized_Data', fontsize=7.5, y=['Fish Spawning Habitats','Nearshore Areas','Great Lakes Tributaries','Great Lakes'])


plt.title("Type of Specialized Data to Collect and Where", fontsize=16)
plt.xticks(rotation=0)


special.set_xlim()
special.set_xlabel("Process")



special.set_ylabel("Count")

plt.show()
