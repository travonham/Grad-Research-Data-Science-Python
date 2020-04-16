import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

basic = pd.read_csv("Basic_Data.csv")
basic.dropna(how='all', inplace=True)

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

basic = basic.plot(kind='barh', color=['blue', 'red','green','black'], x='Data', fontsize=7.5, y=['Fish Spawning Habitats', 'Nearshore Areas', 'Great Lakes Tributaries', 'Great Lakes'])


plt.xticks(rotation=0)
plt.title("Basic Data Collection Areas", fontsize=13)

basic.set_xlabel("Count")


#print(basic)
plt.show()
