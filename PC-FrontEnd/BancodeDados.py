import pandas as pd
from pymongo import MongoClient
from datetime import datetime
from datetime import timedelta
from FunctionsGeneral import LanguagePacket
import pandas as pd

class DatabaseFunctions:
    def __init__(self):
        self.Database = MongoClient()['DDHM']
    def CreateDataBase(self, Language):
        Text=LanguagePacket()
        TextLanguages = Text.DictLanguage()
        Year = datetime(datetime.today().timetuple()[0]-2,1,1).year
        for _ in range(0,9):
            self.Database[str(Year)]
            SalveDB={"Init":"Init"}
            self.Database[str(Year)].insert_one(SalveDB)
            Year = Year+1
        self.Database["Accounts"].insert_one({  "AccountName":TextLanguages[Language]['FirstNameWallet'],
                                                        "Type":0,
                                                        "AccountLimit": 0.0,
                                                        "BalanceAccount": 0.0,
                                                        "PayDay":0,
                                                        "interestMonth":0.0})

        self.Database["Accounts"].insert_one({"_id":"IDs","IDs":0})
        self.Database["Category"].insert_one({"Init":"Init"})
        self.Database["Documents"].insert_one({"Init":"Init"})
        for categorys in TextLanguages[Language]["Categorys"]:
             self.Database["Category"].insert_one({"Name":categorys, "SubCategoryNames":TextLanguages[Language]["Categorys"][categorys]})
    def AddTransation(self,**kwargs):
        NoneorArg = lambda x:(x in kwargs and kwargs.get(x) or None)
        Type                = kwargs.get('Type')
        Value               = kwargs.get('Value')
        Account             = kwargs.get('Account')
        Category            = NoneorArg('Category')
        SubCategory         = NoneorArg('SubCategory')
        Observations        = NoneorArg('Observations')
        Consolidated        = NoneorArg('Consolidated')
        PayDay              = kwargs.get('PayDay')
        FuturePayDay        = NoneorArg('FuturePayDay')
        Alert               = NoneorArg('Alert')
        PaymentVoucherPath  = NoneorArg('PaymentVoucherPath')
        Coin                = NoneorArg('Coin')
        ID = self.Database['Accounts'].find_one({'_id': 'IDs'})['IDs']+1
        TransationDict ={      
                            "Type":Type,
                            "Value":Value,
                            "Account":Account,
                            "Category":Category,
                            "SubCategory":SubCategory,
                            "Observations":Observations,
                            "Consolidated":Consolidated,
                            "PayDay":PayDay,
                            "FuturePayDay":FuturePayDay,
                            "Alert":Alert,
                            "PaymentVoucherPath":PaymentVoucherPath,
                            "Coin":Coin,
                            "_id": ID
        }
        self.Database[PayDay[6:]].insert_one(TransationDict)
        self.Database['Accounts'].update_one({'_id': 'IDs'}, {"$set":{'IDs':ID}})