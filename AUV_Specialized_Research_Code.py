import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#import libraries

special = pd.read_csv("SpecializedData.csv")
#read csv file in/Check file pathway

special.dropna(how='all', inplace=True)
special = special.drop([5], axis = 0, )
#remove row 5 by label name/Start index at labels

special = special.plot(kind='bar', x='Specialized_Data', fontsize=7.5, y=['Fish Spawning Habitats','Nearshore Areas','Great Lakes Tributaries','Great Lakes'])
#plot method for graph

plt.title("Type of Specialized Data to Collect and Where", fontsize=16)
plt.xticks(rotation=0)


special.set_xlim()
special.set_xlabel("Process")
#set X label  name


special.set_ylabel("Count")

plt.show()
