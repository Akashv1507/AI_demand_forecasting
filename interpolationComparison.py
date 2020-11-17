import pandas as pd 
from sklearn.impute import KNNImputer
from sklearn.metrics import r2_score 

df = pd.read_excel("demandFiles/demoOneMonth.xlsx")
# df.reset_index(drop=True, inplace=True)
df.set_index('time', inplace= True)
df['Linear_interpolation'] = df['WR_DEMAND_REF'].interpolate(method='linear')
df['Time_interpolation'] = df['WR_DEMAND_REF'].interpolate(method='time')
df['Slinear_interpolation'] = df['WR_DEMAND_REF'].interpolate(method='slinear')
df['Quadratic_interpolation'] = df['WR_DEMAND_REF'].interpolate(method='quadratic')

linearR2Score = r2_score(df['WR_DEMAND'], df['Linear_interpolation'])
timeR2Score = r2_score(df['WR_DEMAND'], df['Time_interpolation'])
slinearR2Score = r2_score(df['WR_DEMAND'], df['Slinear_interpolation'])
quadraticR2Score = r2_score(df['WR_DEMAND'], df['Quadratic_interpolation'])

print(f" Linear R2 Score is {linearR2Score}")
print(f" Time R2 Score is {timeR2Score}")
print(f" Slinear R2 Score is {slinearR2Score}")
print(f" Quadratic R2 Score is {quadraticR2Score}")
df.to_excel("demandFiles/demoOneMonthRes.xlsx") 