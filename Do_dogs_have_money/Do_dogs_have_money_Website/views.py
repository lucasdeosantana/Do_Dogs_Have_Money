from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	dic = {
			"MonthShow":"Outubro",
			"YearShow":"2020",
			"GeneralInformation":{
				"BalanceSigned":"",
				"Balance":"1500.00",
				"BalancePercenteInformation":"+15",
				"BalanceInformation":"Em relação ao mês anterior",
				"Expenses":"1700,00",
				"ExpensesSignedPercenteInformation":"-",
				"ExpensesPercenteInformation":"15",
				"ExpensesInformation":"Em relação ao mês anterior",
				"Active":"50,00",
				"ActiveSignedPercenteInformation":"-",
				"ActivePercenteInformation":"15",
				"ActiveInformation":"Em relação ao mês anterior",
				"Liabilities":"50,00",
				"LiabilitiesSignedPercenteInformation":"+",
				"LiabilitiesPercenteInformation":"15",
				"LiabilitiesInformation":"Em relação ao mês anterior",
				"DeltaActiveLiabilities":1
			},
			"Accounts":[
				{
					"Name":"Santander",
					"Balance":"25,00",
					"BalanceSigned":"",
					"ProgressBar":True,
					"ProgressBarbg":"red",
					"ProgressBarwidth":100,
					"Color":"red",
				},
				{
					"Name":"Youtube",
					"BalanceSigned":"-",
					"Balance":"225,00",
					"ProgressBar":True,
					"ProgressBarbg":"primary",
					"ProgressBarwidth":100,
					"Color":"primary",
				},
				{
					"Name":"Bradesco",
					"BalanceSigned":"",
					"Balance":"225,00",
					"ProgressBar":True,
					"ProgressBarbg":"primary",
					"ProgressBarwidth":100,
					"Color":"primary",
				},		

			]
		}
	return render(request, 'Do_dogs_have_money_Website/index.htm.j2', dic)
def newTransaction(request):
	return render(request, 'Do_dogs_have_money_Website/newTransaction.htm.j2')