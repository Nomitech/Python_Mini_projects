# Create a Python Calculator to Add, Subtract, Multiply and Divide two numbers with the user given numbers!

# first we just creat a input options

a = int(input("Enter your first number "))
b = int(input("Enter your second number "))

choice = input("Enter your Choice ( + - * / )")

if choice == "+":
    Sum = a + b
    print("The Addition of two number is: ",Sum)

elif choice == "-":
    Sub = a - b
    print("The Subtraction of two number is: ",Sub)
    
elif choice == "*":
    Mul = a * b
    print("The Multiplication of two number is: ",Mul)
    
elif choice == "/":
    Div = a / b
    print("The Division of two number is: ",Div)

else:
    print("Invalid! symbol please try again")

print("...........Thanks for Using this Calculator.........")




