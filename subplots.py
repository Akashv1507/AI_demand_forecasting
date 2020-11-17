import pandas as pd 
import matplotlib.pyplot as plt

demandDf = pd.read_excel("demandFiles/SCADA demand_01_2017 OutliersInterpolated.xlsx")

timestamp = demandDf['time']
wrDemand = demandDf['WR_DEMAND']
mahDemand = demandDf['MSEB_DEMAND']
mumbDemand = demandDf['MUM_DEMAND']
gujDemand = demandDf['GEB_DEMAND']
mpDemand = demandDf['MPSEB_DEMAND']
chattDemand = demandDf['CSEB_DEMAND']
goaDemand = demandDf['GOA_DEMAND']
ddDemand = demandDf['DD_DEMAND']
dnhDemand = demandDf['DNH_DEMAND']

fig, ax = plt.subplots(nrows=4, ncols=2,constrained_layout=True)
la1, = ax[0][0].plot(timestamp, wrDemand,color='#de689f')
la2, = ax[0][1].plot(timestamp, mahDemand, color='#eb3434')
la3, = ax[1][0].plot(timestamp, gujDemand, color='#34ebdf')
la4, = ax[1][1].plot(timestamp, mpDemand, color='#34e2eb')
la5, = ax[2][0].plot(timestamp, chattDemand, color='#c934eb')
la6, = ax[2][1].plot(timestamp, goaDemand, color='#eb3459')
la7, = ax[3][0].plot(timestamp, ddDemand, color='#34ebae')
la8, = ax[3][1].plot(timestamp, dnhDemand, color='#ebba34')

ax[0][0].set_title('WR Demand')
ax[0][0].set_ylabel('MW')

ax[0][1].set_title('MAH Demand')
ax[0][1].set_ylabel('MW')

ax[1][0].set_title('Guj Demand')
ax[1][0].set_ylabel('MW')

ax[1][1].set_title('MP Demand')
ax[1][1].set_ylabel('MW')

ax[2][0].set_title('Chatt Demand')
ax[2][0].set_ylabel('MW')

ax[2][1].set_title('Goa Demand')
ax[2][1].set_ylabel('MW')

ax[3][0].set_title('DD Demand')
ax[3][0].set_ylabel('MW')

ax[3][1].set_title('DNH Demand')
ax[3][1].set_ylabel('MW')


plt.show()