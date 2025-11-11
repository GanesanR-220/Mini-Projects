# Format variables using string.format() method

totalmoney = 1000
quantity = 3
price = 450

statement = "I have {0} dollars so I can buy {1} football for {2:.2f} dollars"
print(statement.format(quantity, totalmoney, price))
