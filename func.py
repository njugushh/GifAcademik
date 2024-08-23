def say_hi(name, age):                       # parameters are values added inside a function
    print(f"Hello {name}, you are {age} years old.")
say_hi("Dan", 25)
    
# * Return Statement - Return information from a function * Haven't grasped it yet *

def cube(num):
    return num * num * num
result = cube(3)
print(result)

# returning a value

def add_numbers(a, b):
    return a + b
result = add_numbers(3, 5)  # stores the returned value
print(result) 

# Return multiple values

def get_user_info():
    name = "Dan"
    age = 25
    return name, age
name, age = get_user_info()   
print(name)
print(age)

#   Early Return

def check_even_or_odd(number): 
    if number % 2 == 0:
        return "Even"
    return "Odd"
result = check_even_or_odd(9)
print(result)


        