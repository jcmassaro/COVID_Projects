import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl
import matplotlib.ticker as ticker

os.chdir('/users/johnmassaro/desktop')
df = pd.read_csv('US-cases.csv', skiprows = 3)
data = {'State/Territory': df['State/Territory'], 'Total Cases': df['Total Cases']}
df1 = pd.DataFrame(data)
x = df1['State/Territory']
y = df1['Total Cases']
y.drop(df.tail(1).index,inplace=True)
x.drop(df.tail(1).index,inplace=True)



figure(num = None, figsize =(30,15), dpi = 100, facecolor = 'white', edgecolor = 'white')



plt.bar(x, height = y, color = (0.9, 0, 0, 0.8))
#ax.get_yaxis().set_major_formatter(mpl.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
plt.xticks(rotation = 90)
plt.title('COVID Cases by State', fontsize = 20)
plt.xlabel('State')
plt.ylabel('Total Cases')
plt.ticklabel_format(style='plain', axis='y', useLocale = True)





#plt.savefig('Covid_Figure2.jpg')

plt.show()

