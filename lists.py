num = [1, 2, 3, 4, 5]
exes = ["Sally", "Gakii", "Marion", "Phancy", "Cynthia"]
exes[2] = "Peris" # modifies/replaces an element inside the list
print(exes[-1]) # Indexing prints exes from the right to left
print(exes[1:3]) # Indexing prints exes from the index you chose onwards upto but not 3

exes.extend(num)  # combines both lists together
print(exes)

num.append(6) # adds data at the end of a list
print(num)

exes.insert(1, "Diana")  # adds the data at the index and pushes the rest to the right
print(exes)

exes.remove("Diana")  # removes a particular element from the list
print(exes)

# friends.clear() - removes every element from the list

num.pop()  # removes the last element on the list
print(num)

print(exes.index("Sally")) # Tells whether the element is in the list or not

print(exes.count("Peris"))  # Counts how many elements of same value are in the list

# exes.sort() - sorts the list in ascending order
# exes.reverse() - reverses the list / rotates the list

exes2 = exes.copy()  # copies the exact list into the the second list
print(exes2)


# 2D LISTS

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in number_grid:
    for col in row:
        print(col, end="")
print(number_grid[2][2])