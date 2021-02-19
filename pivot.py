import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('')

#data = data.pivot(index='data', columns='name',values='dollars')
#data = data.pivot_table(index='data', columns='name',values='dollars')
#print(data)

data_multi = data.set_index(['date','name'])
#print(data_multi.stack())
print(data.T)