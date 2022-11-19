

import pandas as pd
import numpy as np
import glob
import os
    
path = os.getcwd()
files = os.listdir(path)
#print(files)

files_xls = [f for f in files if f[-4:] == 'xlsx']
#print(files_xls)

df = pd.DataFrame()
for f in files_xls:
    data = pd.read_excel(f)
    df = df.append(data)

df.to_excel(r'C:\Users\admin\Desktop\mycourses\mahmoudsaeed\\all.xlsx')
df["Minuts"]=df.iloc[:,1:].sum(axis=1)

print(df)






    