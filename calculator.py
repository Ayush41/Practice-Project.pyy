def calculator():
    print("***Calculator***")
    print("Select Operation")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Division")
    print("4.Multiplication")

    choice = input("Enter choice [1,2,3,4] :")

    if choice in ['1','2','3','4']:
        try:
            num1 = float(input("Enter first number :"))
            num2 = float(input("Enter second number :"))

            if choice == '1':
                print(f"{num1} + {num2} = {num1+num2}")
            elif choice == '2':
                print(f"{num1} + {num2} = {num1-num2}")
            elif choice == '3':
                print(f"{num1} + {num2} = {num1/num2}")
            elif choice == '4':
                print(f"{num1} + {num2} = {num1*num2}")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("Invalid Input!")

calculator()