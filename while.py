#It is a control flow statement that allows code to be executed repeatedly based on a given Boolean condtion
#loop continues to execute as long as condition is true
#basic syntax
# while condition:
    # code block to execute

i = 0
while i < 4:
    print(i)
    i += 1
print("Done with loop")
    
    
# Building a Guessing Game

secret_word = "Njoti"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter Guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("You loose")
else:
    print("Correct!")


