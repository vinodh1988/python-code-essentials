import pandas as pd
import matplotlib.pyplot as plt


data = {
    'years' : [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],
    'production[tons]': [123,543,1233,345,235,256,643,123,1556,123,153,1256]
}

dataframe=pd.DataFrame(data)

print(dataframe)

dataframe.plot(kind='hist',x='years', y='production[tons]')

plt.show()