x = int(input("Please enter first number:"))
y = int(input("Please enter second number:"))
z = input("Please enter action:")

if y == 0 and z == "/":
    print("You can't divide by 0")
elif z == "+":
    print("Your result is:", x + y)
elif z == "-":
    print("Your result is:", x - y)
elif z == "*":
    print("Your result is:", x * y)
elif z == "/":
    print("Your result is:", x / y)
