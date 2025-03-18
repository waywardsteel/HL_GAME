# checks for an integer with optional upper /
# lower limits and an optional exit code for infinite mode
# / quitting the game
def int_check(question, low=None, high=None, exit_code=None):

    # if any integer is allowed
    if low is None and high is None:
        error = "Please enter an integer"

    # if the number needs to be more than an
    #integer (ie. rounds / 'high number')
    elif low is not None and high is None:
        error = (f"please enter an integer that is "
                 f"more than / equal to {low}")

    # if the number needs to be between low & high
    else:
        error = (f"please enter an integer that"
                 f" is between {low} and {high} (inclusive)")

    while True:

        to_check = input(question).lower()

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            to_check = int(to_check)

            #check that the number is more than / equal to 13
            if to_check < 1:
                print(error)
            else:
                return to_check

        except ValueError:
            print(error)

    # Guessing loop

# replace number below with random number between high / low values
secret = 7

# parameters that already exist in base game
low_num = 0
high_num = 10
guesses_allowed = 5

# set guesses used to zero at the start of each round
guesses_used = 0
already_guessed = []

guess = ""
while guess != secret and guesses_used < guesses_allowed:

    #ask user to guess number
    guess = int_check("guess: ", low_num, high_num)

    if guess == "xxx":
        end_game ="yes"
        break

    # check that guess is not a duplicate
    if guess in already_guessed:
        print(f"you've already guessed {guess}. you've *still* used "
              f"{guesses_used} / {guesses_allowed}")
        continue

    # if guess is not a duplicate, add it to the 'already guessed' list
    else:
        already_guessed.append(guess)

     # add one to the number of guesses used
        guesses_used += 1

    # if we have guesses left
    if guess < secret and guesses_used < guesses_allowed:
        print(f"too low, please try a higher number",
                    f"you've used {guesses_used} / {guesses_allowed}")
    elif guess > secret and guesses_used < guesses_allowed:
        print(f"too high, please try a lower number",
                    f"you've used {guesses_used} / {guesses_allowed}")

    #when the secret number is guessed, we have 3 different feedbacks
    elif guess == secret:

        if guesses_used == 1:
            print("🎉🎉🎉Lucky! you got it on the first guess🎉🎉🎉")
        elif guesses_used == guesses_allowed:
            print(f"phew! you got it in {guesses_used} guesses")
        else:
            print(f"well done! you guesses the secret number in {guesses_used} guesses")

    #if there are no guesses left
    else:
        print("sorry - you have no more guesses. you lose this round")


    #additional feedback
    if guesses_used == guesses_allowed - 1:
        print("\n💣💣💣 careful - you only have 1 guess left! 💣💣💣\n")

print()
print("end of round")

