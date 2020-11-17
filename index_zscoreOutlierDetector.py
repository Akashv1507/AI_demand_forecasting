import argparse
from datetime import datetime as dt
from datetime import timedelta
from zscoreOutlierDetector import OutlierDetector

startYear = dt.now() - timedelta(days=1)
batchSize = 1 

# startDate = endDate

# get start and end dates from command line
parser = argparse.ArgumentParser()
parser.add_argument('--start_year', help="Enter Start date in yyyy-mm-dd format",
                    default=dt.strftime(startYear, '%Y-%m-%d'))
parser.add_argument('--batch_size', help="Enter batch size",
                    default=batchSize)
                    
args = parser.parse_args()
startYear = dt.strptime(args.start_year, '%Y-%m-%d')
batchSize = args.batch_size
startYear = startYear.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)

print(batchSize, startYear)

# create minwise demand and purity percentage between start and end dates
obj_outlierDetection = OutlierDetector(startYear)
isoutlierDetectionSuccess = obj_outlierDetection.detectOutlier(startYear, batchSize)

# if isRawDataCreationSuccess:
#     print('raw minwise demand data creation done...')
# else:
#     print('raw minwise demand data creation failure...')