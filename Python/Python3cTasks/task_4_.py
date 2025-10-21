TAX_RATE = 0.06
item1 = input("Enter item 1: ")
price1 = float(input("Enter price 1: "))
tax1 = price1 * TAX_RATE
item2 = input("Enter item 2: ")
price2 = float(input("Enter price 2: "))
tax2 = price2 * TAX_RATE
item3 = input("Enter item 3: ")
price3 = float(input("Enter price 3: "))
tax3 = price3 * TAX_RATE
print()
print(item1, "costs $", round(price1, 2), "with tax $", round(tax1, 2))
print(item2, "costs $", round(price2, 2), "with tax $", round(tax2, 2))
print(item3, "costs $", round(price3, 2), "with tax $", round(tax3, 2))
#gets the prices and items and adds the 6%