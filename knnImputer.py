import pandas as pd 
from sklearn.impute import KNNImputer

df = pd.read_excel("demandFiles/demoKnn.xlsx")

entityList = df.columns.tolist()[3:]
for entity in entityList:
    x = df[entity].to_numpy().reshape(-1,1)
    imputer = KNNImputer(n_neighbors=1)
    val = imputer.fit_transform(x)
    df[entity]= val

df.to_excel("demandFiles/demoKnn.xlsx") 
