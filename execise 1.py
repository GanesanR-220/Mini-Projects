#Exercise 1: Calculate the multiplication and sum of two numbers

def mul_or_sum(num1,num2):
    product = num1 * num2
    if product <=1000:
        return product
    else:
        return num1 + num2

result = mul_or_sum(20, 30)
print("the result is",result)

result = mul_or_sum(100, 30)
print("the result is",result)
