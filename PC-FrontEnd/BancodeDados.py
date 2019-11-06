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
        ID = self.Database['Accounts'].find_one({'_id': 'IDs'})['IDs']+1
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
        self.Database['Accounts'].update_one({'_id': 'IDs'}, {"$set":{'IDs':ID}})
    def delTransation(self, ID, PayDay):
        pass
    def CreateDataFrame(self,InitialDay=0, EndDay=0):
        if('Transations' in self.Database.list_collection_names()):
            SheetwithTransation = pd.DataFrame(list(self.Database['Transations'].find()))
            return SheetwithTransation
        else:
            return -1
    def AddInstallment(self,**kwargs):
        InitialInstallment = kwargs.get('InitialInstallment')
        EndInstallment = kwargs.get('EndInstallment')
        kwargs.get('FuturePayDay')
        for x in range(InitialInstallment, EndInstallment):
            kwargs['InitialInstallment'] = x
            self.AddTransation(**kwargs)
            kwargs['FuturePayDay']=self.DateFormate(kwargs.get('FuturePayDay'))
    def DateFormate(self, Date):
        Day = int(Date[0:2])
        Month = int(Date[3:5])+1
        year = int(Date[6:])
        if(Month>12):
            Month = 1
            year+=1
        if(Day<10):
            day = '0'+str(Day)
        else:
            day = str(Day)
        if(Month<10):
            month = '0'+str(Month)
        else:
            month = str(Month)   
        return (day+'/'+month+'/'+str(year))