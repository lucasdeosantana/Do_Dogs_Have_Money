function SubCategory(){
    var category = document.getElementById("Categorys")
    var subcategory = document.getElementById("subcategory")
    console.log()
}
function OpenTransaction() {
	document.getElementById("newtransaction").style.display ="block"
	document.getElementById("mainbodys").style.display ="none"
	formExpense()
}
function closeTransaction() {
	document.getElementById("newtransaction").style.display ="none"
	document.getElementById("mainbodys").style.display =""
}
function formExpense(){
	removeForm()
	document.getElementById("ExpenseForm").style.display=""
}
function formTransfer(){
	removeForm()
	document.getElementById("TransferForm").style.display=""
}
function formReceive(){
	removeForm()
	document.getElementById("RecipesForm").style.display=""
}
function Datebug(){
	var DatePicker=document.getElementById("datepicker")
	DatePicker.value=DatePicker.value[3]+DatePicker.value[4]+DatePicker.value[2]+DatePicker.value[0]+DatePicker.value[1]+DatePicker.value[2]+DatePicker.value[6]+DatePicker.value[7]+DatePicker.value[8]+DatePicker.value[9]
}
function Datebug2(){
	document.getElementsByClassName("bootstrap-datetimepicker-widget dropdown-menu bottom")[0].remove()
	}
function Valuesigned(){
	var InputValue = document.getElementById("InputValue")
	if(InputValue.value>0){
		InputValue.value= InputValue.value*-1
	}
}
function removeForm(){
	document.getElementById("RecipesForm").style.display="none"
	document.getElementById("TransferForm").style.display="none"
	document.getElementById("ExpenseForm").style.display="none"

}
function RepeatChange(){
	var repeatform = document.getElementById("Repeatform")
	if(document.getElementById("checkbox1").checked){
		repeatform.style.display=""
	}else{
		repeatform.style.display="none"
	}
}