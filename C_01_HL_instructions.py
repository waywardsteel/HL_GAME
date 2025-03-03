# checks user enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "no":
           return "no"
        else:
            print("please enter yes / no")


def instructions():
    print('''
    
**** Instructions ****

To begin, choose the number of rounds and either customise 
the game parameters or go with the default game (where the 
secret number will be between 1 and 100)

Then choose how many rounds you'd like to play <enter> for 
infinite mode.

Your goal is to guess the secret number without
running out of guesses.

Good luck.
 
    ''')


# Main routine
print()
print("⬆️⬆️⬆️Welcome to higher or lower game ⬆️⬆️⬆️")
print()

#loop for testing

want_instructions = yes_no("do you want instruction")

# checks user enters yes / no
if want_instructions == "yes":
    instructions()

print("program continues")