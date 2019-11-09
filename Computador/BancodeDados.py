import pandas as pd
from pymongo import MongoClient
from datetime import datetime
from datetime import timedelta
from FunctionsGeneral import LanguagePacket

class DatabaseFunctions:
    def __init__(self):
        self.Database = MongoClient()['DDHM']
    def CreateDataBase(self, Language):
        Text=LanguagePacket()
        TextLanguages = Text.DictLanguage()
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
    def AddTransaction(self,ID=None,**kwargs):
        NoneorArg = lambda x:(x in kwargs and kwargs.get(x) or None)
        Type                = kwargs.get('Type')
        if(Type == 1):
            Value = kwargs.get('Value')*-1
        else:
            Value = kwargs.get('Value')
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
        InitialInstallment  = NoneorArg('InitialInstallment')
        EndInstallment      = NoneorArg('EndInstallment')
        if(ID==None):
            ID = self.Database['Accounts'].find_one({'_id': 'IDs'})['IDs']+1
            self.Database['Accounts'].update_one({'_id': 'IDs'}, {"$set":{'IDs':ID}})
        if(Type == 0):
            AccountDestiny = kwargs.get('AccountDestiny')
        else:
            AccountDestiny = None
        TransationDict ={
                            "Type":Type,
                            "Value":Value,
                            "Account":Account,
                            "AccountDestiny":AccountDestiny,
                            "Category":Category,
                            "SubCategory":SubCategory,
                            "Observations":Observations,
                            "Consolidated":Consolidated,
                            "PayDay":PayDay,
                            "FuturePayDay":FuturePayDay,
                            "Alert":Alert,
                            "PaymentVoucherPath":PaymentVoucherPath,
                            "Coin":Coin,
                            "_id": ID,
                            "InitialInstallment":InitialInstallment,
                            "EndInstallment":EndInstallment
        }
        self.Database['Transations'].insert_one(TransationDict)
    def delTransaction(self, ID):
        self.Database['Transations'].delete_one({"_id":ID})
    def editTransaction(self,ID,**kwargs):
        delTransaction(ID,**kwargs)
        AddTransaction(ID,**kwargs)
    def CreateDataFrame(self,InitialDay=0, EndDay=0):
        if('Transations' in self.Database.list_collection_names()):
            SheetwithTransation = pd.DataFrame(list(self.Database['Transations'].find()))
            return SheetwithTransation
        else:
            return -1
