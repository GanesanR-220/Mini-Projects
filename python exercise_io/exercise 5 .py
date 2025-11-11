# Accept a list of 5 float numbers as an input from the user

numbers = []

for i in range(1,6):
    print("Enter a Number", i, ':')

    item = float(input())
    numbers.append(item)

print("User List:", numbers)