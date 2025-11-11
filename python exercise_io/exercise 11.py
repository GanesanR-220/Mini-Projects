# percentage display

try: 
    numerator = float(input("enter the numerator:"))
    denominator = float(input("enter the denominator:"))
    if denominator == 0:
        print("Error: Denominator cannot be zero")
    else:
        percentage = (numerator / denominator) * 100
        print(f"the percentage id :{percentage:.2f}%")
except ValueError:
    Print("Invalid input. please enter number.")