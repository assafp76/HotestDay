import pandas as pd
files_location = r'C:\Users\user\Downloads\DLG'
df1 = pd.read_csv(files_location+'\weather.20160201.csv')
df2 = pd.read_csv(files_location+'\weather.20160301.csv')
df = df1.append(df2, ignore_index=True)
df['obdate']  = df.ObservationDate.str[:10]
series_day_max = df.groupby(['obdate','Region','Country'])['ScreenTemperature'].max().reset_index()
series_day_max.sort_values(by='ScreenTemperature',ascending=False).head()