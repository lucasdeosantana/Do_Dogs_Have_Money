from django.db import models

# Create your models here.
class Transaction(models.Model):
	Transaction_Value = models.IntegerField()
	Transaction_Date = models.DateField() 
	Transaction_Category = models.ForeignKey('Category',on_delete=models.CASCADE)
	Transaction_Account = models.ForeignKey('DB_Accounts',on_delete=models.CASCADE)

class DB_Accounts(models.Model):
	Account_name = models.CharField(max_length=255)
	Account_type = models.IntegerField()
	Account_balance = models.IntegerField()
	Account_limit = models.IntegerField()
	Account_payday = models.IntegerField()

class Category(models.Model):
	Category_name = models.CharField(max_length=255)
