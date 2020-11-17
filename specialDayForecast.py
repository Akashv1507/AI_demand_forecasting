import pandas as pd 
import cx_Oracle
from typing import List, Tuple

specialForecastDf = pd.read_excel("demandFiles/10-11-2020.xlsx")

columns = specialForecastDf.columns.tolist()[1:]
demandList:List[Tuple] = []
demandListR0A:List[Tuple] = []

for ind in specialForecastDf.index:
    for entity in columns:
        tempTuple = (specialForecastDf['Time'][ind], entity, specialForecastDf[entity][ind])
        demandList.append(tempTuple)

        tempTupleR0A = (specialForecastDf['Time'][ind], entity, 'R0A', specialForecastDf[entity][ind])
        demandListR0A.append(tempTupleR0A)

# making list of tuple of timestamp(unique),entityTag based on which deletion takes place before insertion of duplicate

existingRows = [(x[0],x[1]) for x in demandList]
existingRowsR0A = [(x[0],x[1], x[2]) for x in demandListR0A]
# print(demandList)
# print(demandListR0A)
try:  
    connection = cx_Oracle.connect('mis_warehouse/wrldc#123@10.2.100.56:15210/ORCLWR')
    isInsertionSuccess = True

except Exception as err:
    print('error while creating a connection', err)
else:
    try:
        cur = connection.cursor()
        try:
            cur.execute("ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD HH24:MI:SS' ")
            del_sql = "DELETE FROM dayahead_demand_forecast WHERE time_stamp = :1 and entity_tag=:2"
            cur.executemany(del_sql, existingRows)
            insert_sql = "INSERT INTO dayahead_demand_forecast(time_stamp,ENTITY_TAG,forecasted_demand_value) VALUES(:1, :2, :3)"
            cur.executemany(insert_sql, demandList)

            # stroing R0A
            del_sql = "DELETE FROM forecast_revision_store WHERE time_stamp = :1 and entity_tag=:2 and revision_no =:3"
            cur.executemany(del_sql, existingRowsR0A)
            insert_sql = "INSERT INTO forecast_revision_store(time_stamp,ENTITY_TAG,revision_no,forecasted_demand_value) VALUES(:1, :2, :3, :4)"
            cur.executemany(insert_sql, demandListR0A)
        except Exception as e:
            print("error while insertion/deletion->", e)
            isInsertionSuccess = False
    except Exception as err:
        print('error while creating a cursor', err)
        isInsertionSuccess = False
    else:
        connection.commit()
finally:
    cur.close()
    connection.close()
    print("dayahead demand forecast insertion/ R0A revision storage complete")



