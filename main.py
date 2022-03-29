from matplotlib import pyplot as plt

from dataframe import dataframe

dataframe('TSLA', '2020-03-01', '2022-03-01', 'red')
dataframe('MSFT', '2020-03-01', '2022-03-01', 'black')
dataframe('AAPL', '2020-03-01', '2022-03-01', 'blue')
plt.show()
