import pandas as pd
import numpy as np
from scipy import stats
df=pd.read_csv('data.csv')
df['zscores']=(df.Calories-df.Calories.mean())/df.Calories.std()
df[df['zscores']>3]
