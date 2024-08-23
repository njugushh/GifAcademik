num_1 = float(input("What is the first number: "))
num_2 = float(input("What is the second number: "))
result = num_1 * num_2       # You can also add int/float here instead

print(result)

# Advanced calculator using if statement

num1 = float(input("What is first number: "))
op = input("What is operator: ")
num2 = float(input("What is the second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid Operator")
    
    
    