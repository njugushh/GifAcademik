#if condtion - used to execute a block of code only if specified condtion is true
# or - it becomes true if one of the values is true and false if all values are not true
#and - becomes true if all are true and false if either is not true
# basic syntax
# if condition:
    # code block to execute if condition is true

is_male = False  # Bool - Booleans are eithere true or false
is_tall = True
if is_male and is_tall:
    print( "You are a tall male")
elif is_male and not(is_tall):               # You can still use () to negate the false statements
    print("you are a short male")
elif not is_male and is_tall:
    print("you are a tall female")   # you can put a lot of code in the if statement
else:
    print("You are not male and not tall or both")
    
    
# COMPARISON - !=<>

def min_num(num1, num2, num3):
    if num1<=num2 and num1<=num3:
        return num1
    elif  num2<=num1 and num2<=num3:
        return num2
    return num3
result = min_num(200, 12, 3)
print(result)




