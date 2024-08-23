# Handles errors in a code and stops us from crashing the code
# Always be catching specific errors

try:
    value = 10 / 0
    number = (int(input("Enter a number: ")))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invaid Input")