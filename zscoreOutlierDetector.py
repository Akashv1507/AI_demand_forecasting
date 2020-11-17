# from datetime import datetime as dt
import datetime as dt
import pandas as pd 
import numpy as np

class OutlierDetector():
    def __init__(self, startYear:dt.datetime):
        self.yearString = str(startYear)
        self.xcelFilename = "SCADA demand_01_" + self.yearString[:4] + ".xlsx"
        self.xcelOutputFileName = "SCADA demand_01_" + self.yearString[:4] + " OutliersDetected" + ".xlsx"
        self.xcelFileFullPath = "demandfiles/" + self.xcelFilename
        self.xcelOutputFilePath = "demandfiles/" + self.xcelOutputFileName
        
        self.demandDf = pd.read_excel(self.xcelFileFullPath)

        #initializing storage empty dataframe that append demand values of all entities
        self.afterOutliersDetDemandDf = pd.DataFrame(columns = [ 'time', 'WR_DEMAND', 'MSEB_DEMAND', 'MUM_DEMAND', 'GEB_DEMAND', 'MPSEB_DEMAND', 'CSEB_DEMAND', 'GOA_DEMAND', 'DD_DEMAND', 'DNH_DEMAND'])
         


    def computeZscore(self, startTime:dt.datetime, endTime:dt.datetime):

        entityDemandDf = self.demandDf[(self.demandDf['time']>= startTime) &  (self.demandDf['time']<= endTime)]
        listOfEntity = ['WR_DEMAND', 'MSEB_DEMAND', 'MUM_DEMAND', 'GEB_DEMAND', 'MPSEB_DEMAND', 'CSEB_DEMAND', 'GOA_DEMAND', 'DD_DEMAND', 'DNH_DEMAND']
        
        #iterating through each entity
        for entity in listOfEntity:
            threshold = 3
            meanOfDay = entityDemandDf[entity].mean()
            stdDeviationOdDay = entityDemandDf[entity].std()

            #iterating through each value of entity 
            for ind in entityDemandDf.index:
                z = (entityDemandDf[entity][ind]-meanOfDay)/stdDeviationOdDay
                if abs(z) > threshold: 
                    entityDemandDf[entity][ind] = np.nan
        return entityDemandDf



    def detectOutlier(self, startDate:dt.datetime, bathcSize:int):

        
        lastDayOfYear = startDate.replace(month= 12, day = 31)
        currDate = startDate

        #iterating to last day of year based on batch size
        while currDate <= lastDayOfYear:
            startTime = currDate.replace(hour=0, minute=0, second=0, microsecond=0)
            endTime = startTime + dt.timedelta(hours= 23, minutes= 59)
            outlierDetectedDf =self.computeZscore(startTime, endTime)
            self.afterOutliersDetDemandDf = pd.concat([self.afterOutliersDetDemandDf, outlierDetectedDf], ignore_index=True)
            currDate =currDate + dt.timedelta(days=int(bathcSize))

        self.afterOutliersDetDemandDf.set_index('time', inplace= True)
        self.afterOutliersDetDemandDf.to_excel(self.xcelOutputFilePath)



    

