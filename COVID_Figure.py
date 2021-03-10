#Imports needed to get data and turn into a bar chart
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl
import matplotlib.ticker as ticker

#Accessing CSV downloaded from CDC.gov
os.chdir('/users/johnmassaro/desktop')
df = pd.read_csv('US-cases.csv', skiprows = 3)

#focusing on States/Territories and Cases, ignoring other data points
data = {'State/Territory': df['State/Territory'], 'Total Cases': df['Total Cases']}
df1 = pd.DataFrame(data)
x = df1['State/Territory']
y = df1['Total Cases']

#Dropping totals at end so they don't skew chart
y.drop(df.tail(1).index,inplace=True)
x.drop(df.tail(1).index,inplace=True)


#Creating chart
figure(num = None, figsize =(30,15), dpi = 100, facecolor = 'white', edgecolor = 'white')

plt.bar(x, height = y, color = (0.9, 0, 0, 0.8))
plt.xticks(rotation = 90)
plt.title('COVID Cases by State', fontsize = 20)
plt.xlabel('State')
plt.ylabel('Total Cases')
plt.ticklabel_format(style='plain', axis='y', useLocale = True)




#Line to save figure
#plt.savefig('Covid_Figure2.jpg')

plt.show()

