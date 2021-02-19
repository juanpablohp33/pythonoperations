import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
import seaborn as sns
from sklearn.cluster import DBSCAN

my_data = pd.read_csv("C:\\Users\\Juan Pablo Hernandez\\Desktop\\PYTHON\\olympics.csv", header=1)
pd.set_option("display.max_rows", None,"display.max_columns", None)

new_names = {'Unnamed: 0' : 'Country',
              '№ Summer' : 'Summer Olympics', 
              '01 !' : 'Gold', 
              '02 !' : 'Silver', 
              '03 !' : 'Bronze',  
              '№ Winter': 'Winter Olympics',
              '01 !.1' : 'Gold.1', 
              '02 !.1' : 'Silver.1', 
              '03 !.1' : 'Bronze.1',  
              '№ Games' : 'Games', 
              '01 !.2' : 'Gold.2', 
              '02 !.2' : 'Silver.2',
              '03 !.2' : 'Bronze.2'}

my_data.rename(columns=new_names,inplace=True)

column_names = my_data.columns
print(column_names)

print(my_data['Silver'].isnull())

my_data = my_data.dropna(thresh = int(my_data.shape[0]*.9),axis=1)
print(my_data.head(3))

new = np.where(my_data.Country.str.contains('!'), my_data.Country.str.replace('!',''),my_data.Country.str.replace('!',''))
new = pd.DataFrame(new)
new.columns = ["Country"]

my_data.Country = new.Country
#print(my_data.head(3))

print(my_data.isna())

my_data.fillna(0,inplace=True)

my_data.drop_duplicates(inplace=True)

print(my_data.duplicated())
