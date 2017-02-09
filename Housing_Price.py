
# coding: utf-8

# In[144]:

import pandas as pd
from __future__ import division
#remove columns with more than half the data missing. Replace Nan in categorical columns with most 
#frequent category if this category comes up more often then 2x the second most frequent category. 
df = pd.read_csv('train.csv')
for col in df.columns.values[1:]:
    if df[str(col)].value_counts().sum() < len(df) /2:
        del df[str(col)]
    else:
        if type(df[str(col)].value_counts().index[0]) is str:
            if df[str(col)].value_counts()[0] - df[str(col)].value_counts()[1] > df[str(col)].value_counts()[0] / 2:
                df[str(col)].fillna(df[str(col)].value_counts().index[0], inplace = True) 
#print the value and counts of all the columns with missing values. 
for titles in df.columns.values[1:]:
    if int(df[['Id', str(titles)]].groupby([str(titles)]).count().sum()) < len(df):
        print df[['Id', str(titles)]].groupby([str(titles)]).count()
        print int(df[['Id', str(titles)]].groupby([str(titles)]).count().sum())


# In[ ]:



