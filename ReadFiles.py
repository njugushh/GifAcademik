# r - read only, r+ - read and write
# we can store it in a variable
# whenever you open a file ensure you close it as well

exes_pandora_box = open("exes.txt", "r")

# print(exes_pandora_box.readlines()[1]) 
# .readable() - returns bool to show if its readable
# .readline() - reads each line.Repeatable / .readlines() - reads and puts them in a list
# .read()

for ex in exes_pandora_box.readlines():
    print(ex)

exes_pandora_box.close()
