import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series([1,3,5,np.nan,6,8])
print (s)

dates = pd.date_range('20130101',periods = 6)
print (dates)

df = pd.dataframe(np.ramdom.ramdn(6,4),index = dates,columns = ('ABCD))
print(df)

df2 = pd.DataFrame{'A' : 1.,
                   'B' : pd.Timestamp('20130102')
                   tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                                        ....:                      'foo', 'foo', 'qux', 'qux'],
....: ['one', 'two', 'one', 'two',
       ....:                      'one', 'two', 'one', 'two']]))


print (1 & int(2) >> 0)

x