import pandas as pd 
from sklearn.impute import KNNImputer
from sklearn.metrics import r2_score 

df = pd.read_excel("demandFiles/SCADA demand_01_2019 OutliersDetected.xlsx")
# df.reset_index(drop=True, inplace=True)
df.set_index('time', inplace= True)

entityList = df.columns.tolist()

for entity in entityList:
    df[entity] = df[entity].interpolate(method='time')


df.to_excel("demandFiles/SCADA demand_01_2019 OutliersInterpolated.xlsx") 