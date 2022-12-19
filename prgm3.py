import pandas as pd
df=pd.read_csv('data.csv')
dup=df.duplicated().sum()
print("number of duplicate rows:",dup,)
print("number of rows in DataFrame:",df.shape)
df_new=df
df_new=df.drop_duplicates()
dup1=df_new.duplicated().sum()
print('number of duplicate rows after deleting values:',dup1)
print('number of rows in DataFrame:',df_new.shape)
