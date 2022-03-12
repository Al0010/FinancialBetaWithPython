import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import math 

# Create Dataframes
df3 = pd.DataFrame()
df4 = pd.DataFrame()

# Start Date
start = dt.datetime(2022,1,1)

# End Date
end = dt.datetime.now()

# Setting ticker 
asset = 'TSLA'
index = '^IXIC'

# Download Data from Yahoo Finance
df1 = web.DataReader(asset, 'yahoo', start, end)
df2 = web.DataReader(index, 'yahoo', start, end)

# Select "AdjClose"
df3['Rendimenti'] = df1['Adj Close'].pct_change()
df4['Rendimenti'] = df2['Adj Close'].pct_change()

# Delete Na
df3.dropna(inplace = True)
df4.dropna(inplace = True)

# Calculate covariance
cov = df3['Rendimenti'].cov(df4['Rendimenti'])

# Calculate variance
var = df4['Rendimenti'].var()

# Calculate beta 
beta = cov/var
print('Beta is... ' + str(beta))
