def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero!"

print("Welcome to the Calculator!")

# The while loop keeps the program running
while True:
    print("\nOperations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice in ("1", "2", "3", "4"):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            if choice == "1":
                result = add(num1, num2)
                print(f"{num1} + {num2} = {result}")
            elif choice == "2":
                result = subtract(num1, num2)
                print(f"{num1} - {num2} = {result}")
            elif choice == "3":
                result = multiply(num1, num2)
                print(f"{num1} * {num2} = {result}")
            elif choice == "4":
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
                
        except ValueError:
            print("Please enter valid numbers!")
            
    elif choice == "5":
        print("Thanks for using the Calculator! Goodbye!")
        break  # This stops the while loop
    
    else:
        print("Invalid choice! Please enter 1, 2, 3, 4, or 5.")