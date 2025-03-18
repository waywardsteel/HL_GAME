import math


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


# Check that users have entered an integer more then 0
def int_check(question, low=None, high=None, exit_code=None):

    # if any integer is allowed
    if low is None and high is None:
        error = "Please enter an integer"

    # if the number needs to be more than an
    # integer (ie. rounds / 'high number')
    elif low is not None and high is None:
        error = (f"please enter an integer that is "
                 f"more than / equal to {low}")

    # if the number needs to be between low & high
    else:
        error = (f"please enter an integer that"
                 f" is between {low} and {high} (inclusive)")

    while True:
        error = input(question).lower()

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # check that the number is more than / equal to 13
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# calculate the number of guesses allowed
def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses


# Main routine starts here

# Intialise game variables
mode = "regular"
rounds_played = 0
end_game = "no"
feedback = ""

game_history = []
all_score = []


print("⬆️⬆️⬆️Welcome to higher or lower game ⬆️⬆️⬆️")
print()

want_instructions = yes_no("do you want instruction")

# checks user enters yes / no
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("Rounds <enter for infinite>: ",
                       low=1, exit_code="")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Get game parameters
low_num = int_check("low number? ")
high_num = int_check("high number? ", low=low_num+1)
guesses_allowed = calc_guesses(low_num, high_num)



# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings
    if mode == "infinite":
        rounds_heading = f"\n🪨📄✂  Round {rounds_played + 1} (Infinite Mode) 🪨📄✂ "
    else:
        rounds_heading = f"\n🪨📄✂  Round {rounds_played + 1} of {num_rounds} 🪨📄✂ "

    print(rounds_heading)
    print()

    user_choice = input("choose: ")

    if user_choice == "xxx":
        break

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1



# Game loop ends here


#game History / statistics area

# calculate lowest, highest and average
# scores and display them
if rounds_played > 0:

    # calculate statistics
    all_score.sort()
    best_score = all_score[0]
    worst_score = all_score[-1]
    average_score = sum(all_score) / len(all_score)

    #output the stats
    print("\n📊📊📊 Statistics 📊📊📊")
    print(f"Best:{best_score} | Worst:{worst_score} | Average:{average_score:.2f} ")
    print()

    # display the game history on request
    see_history = yes_no(" Do you want to see your game history? ")
    if see_history == "yes":
        for item in game_history:
            print()
