print("----------WELCOME----------")
SALARY = 800

seller_number = int(input("Please enter the number of the seller:"))
sales_quantity = int(input("Please enter the quantity of sales:"))
total_value = int(input("Please enter the total value:"))

commission = (50 * sales_quantity) + (5 * total_value) / 100
seller_salary = SALARY + commission

print("Number of seller:", seller_number)
print("Salary:", seller_salary)

