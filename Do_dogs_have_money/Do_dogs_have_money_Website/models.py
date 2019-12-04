from django.db import models

# Create your models here.
class Transaction(models.Model):
	Transaction_Value = models.IntegerField()
	Transaction_Date = models.DateField() 
	Transaction_Category = models.ForeignKey('Category',on_delete=models.CASCADE)
	Transaction_Account = models.ForeignKey('Accounts',on_delete=models.CASCADE)
	Transaction_texte = models.CharField(max_length=500, blank=True, null=True)

class Accounts(models.Model):
	Account_type = (
		(1, 'Wallet'),
		(2, 'Account'),
		(3, 'CreditCar'),
		(4, 'Account With Limit'),
	)
	Account_name = models.CharField(max_length=255)
	Account_Dayfinsh= models.IntegerField(blank=True, null=True)
	Account_type = models.IntegerField(choices=Account_type)
	Account_balance = models.IntegerField()
	Account_limit = models.IntegerField(blank=True, null=True)
	Account_payday = models.IntegerField(blank=True, null=True)
	

	def __str__(self):
		return self.Account_name
	

class Category(models.Model):
	Category_name = models.ForeignKey("Category",on_delete=models.CASCADE)
	subCategory_name = models.CharField(max_length=255)
	def __str__(self):
		return self.subCategory_name
