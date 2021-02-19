import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("C:\\Users\\Juan Pablo Hernandez\\Desktop\\PYTHON\\olympics.csv", header=1)

pd.set_option("display.max_rows", None,"display.max_columns", None)

#print(data.head(10))
#print(data.columns.isnull())
#print(data['03 !'].isnull())
print(data['02 !'].isnull())