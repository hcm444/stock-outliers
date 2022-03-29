import numpy as np
import yfinance as yf
from matplotlib import pyplot as plt

from outliers import indentify_outliers


def dataframe(stock, start_date, end_date, stock_color):
    dframe = yf.download(stock, start=start_date, end=end_date, progress=False).loc[:, ['Adj Close']]
    dframe.rename(columns={'Adj Close': 'adj_close'}, inplace=True)
    dframe['simple_rtn'] = dframe.adj_close.pct_change()
    df_rolling = dframe[['simple_rtn']].rolling(window=21) \
        .agg(['mean', 'std'])
    # calculate the standard deviation
    df_rolling.columns = df_rolling.columns.droplevel()
    # rolling mean
    df_outliers = dframe.join(df_rolling)
    df_outliers['outlier'] = df_outliers.apply(indentify_outliers, axis=1)
    outliers = df_outliers.loc[df_outliers['outlier'] == 1, ['simple_rtn']]
    fig, chart = plt.subplots()
    # plotting the results
    chart.plot(df_outliers.index, df_outliers.simple_rtn, color=stock_color, label='Normal')
    chart.scatter(outliers.index, outliers.simple_rtn, color='red', label='Anomaly')
    chart.set_title(stock + " STOCK RETURNS")
    chart.legend(loc='lower right')
    return chart
