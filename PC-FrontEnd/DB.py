import pandas as pd
from pymongo import MongoClient
from datetime import datetime
from datetime import timedelta

def CreateDataBase(Language):
    
    Database = MongoClient()
    InitialtoEndDay = datetime(datetime.today().timetuple()[0]-2,1,1)
    for month in range(1,120):
        CurrentMonth = InitialtoEndDay.timetuple()[1]
        for day in range(1,32):
            AnalyzedMonth = InitialtoEndDay.timetuple()[1]
            if(CurrentMonth == AnalyzedMonth):
                Database['DDHM'][InitialtoEndDay.strftime('%m/%Y')]
                SalveDB={ "_id":InitialtoEndDay.strftime('%d/%m/%Y'), "DayBalance":0.0, "DayBalanceAccount":{TextLanguages[Language]['FirstNameWallet']:0.0}}
                Database['DDHM'][InitialtoEndDay.strftime('%m/%Y')].insert_one(SalveDB)
                InitialtoEndDay = InitialtoEndDay+timedelta(days=1) 
    Database['DDHM']["Accounts"].insert_one({"AccountName":TextLanguages[Language]['FirstNameWallet'], "Type":0, "AccountLimit": 0.0, "BalanceAccount": 0.0,
                                                "PayDay":0,
                                                "interestMonth":0.0})
    Database['DDHM']["Accounts"].insert_one({"Init":"Init"})
    Database['DDHM']["Category"].insert_one({"Init":"Init"})
def ReturnDataFramePandas():
    ClientMongo = MongoClient()

