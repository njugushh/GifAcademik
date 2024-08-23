# for loop - iterates over the items of a collection,performing an action for each item.
# Basic syntax
# for item in iterable:
    #code block to execute
    
for letter in "Giraffe Academy":
    print(letter)
    
exes = ["Marion", "Sally", "Phancy"]
for index in range(len(exes)):   # doesn't include the last digit
    print(exes[index])
    
for mine in range(5):
    if mine == 0:
        print("First")
    else:
        print("Not First")
        
