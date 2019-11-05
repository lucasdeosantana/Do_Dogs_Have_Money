import pandas as pd
from pymongo import MongoClient
from datetime import datetime
from datetime import timedelta
from FunctionsGeneral import LanguagePacket


class DatabaseFunctions:
    def __init__(self):
        self.Database = MongoClient()
    def CreateDataBase(self, Language):
        Text=LanguagePacket()
        TextLanguages = Text.DictLanguage()
        InitialtoEndDay = datetime(datetime.today().timetuple()[0]-2,1,1)
        for month in range(1,120):
            CurrentMonth = InitialtoEndDay.timetuple()[1]
            for day in range(1,32):
                AnalyzedMonth = InitialtoEndDay.timetuple()[1]
                if(CurrentMonth == AnalyzedMonth):
                    self.Database['DDHM'][InitialtoEndDay.strftime('%m/%Y')]
                    SalveDB={ "_id":InitialtoEndDay.strftime('%d/%m/%Y'), "DayBalance":0.0, "DayBalanceAccount":{TextLanguages[Language]['FirstNameWallet']:0.0}}
                    self.Database['DDHM'][InitialtoEndDay.strftime('%m/%Y')].insert_one(SalveDB)
                    InitialtoEndDay = InitialtoEndDay+timedelta(days=1) 
        self.Database['DDHM']["Accounts"].insert_one({"AccountName":TextLanguages[Language]['FirstNameWallet'], "Type":0, "AccountLimit": 0.0, "BalanceAccount": 0.0,
                                                    "PayDay":0,
                                                    "interestMonth":0.0})
        self.Database['DDHM']["Accounts"].insert_one({"Init":"Init"})
        self.Database['DDHM']["Category"].insert_one({"Init":"Init"})
        for categorys in TextLanguages[Language]["Categorys"]:
             self.Database['DDHM']["Category"].insert_one({"Name":categorys, "SubCategoryNames":TextLanguages[Language]["Categorys"][categorys]})
