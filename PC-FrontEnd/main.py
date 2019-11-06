from BancodeDados import DatabaseFunctions
Database = DatabaseFunctions()
Database.CreateDataBase(Language='Portuguese')
Database.AddTransation(Type=0,Value=10,Account="Minha Carteira",PayDay="27/02/2018")
Database.AddTransation(Type=0,Value=10.25,Account="Minha Carteira",PayDay="27/01/2019")
Transations = Database.CreateDataFrame()
print(Transations)