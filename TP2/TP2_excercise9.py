print("----------WELCOME----------")
money_amount = int(input("Please enter the amount of money:"))

bill_100 = money_amount // 100
rest = money_amount % 100
bill_50 = rest // 50
rest = rest % 50
bill_10 = rest // 10
rest = rest % 10
bill_5 = rest // 5
rest = rest % 5
bill_1 = rest // 1

print("The cashier has to give:")
print(bill_100," bills of 100")
print(bill_50, "bills of 50")
print(bill_10, "bills of 10")
print(bill_5, "bills of 5")
print(bill_1, "bills of 1")


