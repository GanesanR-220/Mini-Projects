# interactive Menu

while True:
    print("\n*****Menu*****")
    print("1. Say Hello")
    print("2. Calculate Square")
    print("3. Exit")

    choice = input("Enter Your Choice (1-3): ")

    if choice == '1':
        print("Hello there!")
    elif choice == '2':
        try:
            number  = int(input("enter a number:"))
            square = number ** 2
            print(f"The square of {number} is {square}")
        except ValueError:
            print("Invalid Error. Pleasse enter an integer")
    elif choice =='3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. please enter a number between 1 and 3.")