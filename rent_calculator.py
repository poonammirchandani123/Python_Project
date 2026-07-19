# Rent Calculator

print("🏠 Welcome to the Rent Calculator")

rent = int(input("Enter your monthly rent (£): "))
food = int(input("Enter the food expense (£): "))
electricity_units = int(input("Enter the electricity units used: "))
charge_per_unit = int(input("Enter the charge per electricity unit (£): "))
persons = int(input("Enter the number of people sharing: "))

electricity_bill = electricity_units * charge_per_unit

total_expense = rent + food + electricity_bill

each_person = total_expense / persons

print("\n----- Bill Summary -----")
print("Rent: £", rent)
print("Food: £", food)
print("Electricity Bill: £", electricity_bill)
print("Total Expense: £", total_expense)
print("Each Person Pays: £", each_person)