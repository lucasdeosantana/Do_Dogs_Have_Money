from BancodeDados import DatabaseFunctions
from FunctionsGeneral import FunctionsGeneral
class Transactions:
    def __init__(self):
        self.FunctionsofDatabase = DatabaseFunctions()
        self.GeneralFunctions = FunctionsGeneral()
    def AddInstallment(self,**kwargs):
        InitialInstallment = kwargs.get('InitialInstallment')
        EndInstallment = kwargs.get('EndInstallment')
        kwargs.get('FuturePayDay')
        for x in range(InitialInstallment, EndInstallment):
            kwargs['InitialInstallment'] = x
            self.FunctionsofDatabase.AddTransation(**kwargs)
            kwargs['FuturePayDay']=self.GeneralFunctions.DateFormate(kwargs.get('FuturePayDay'))