def intcheck(question, low=None, high=None, exit_code=None):

    #if any integer is allowed
    if low is None and high is None:
        error = "please enter an integer"

    # if the number needs to be more than an
    # integer (ie: rounds / 'high number')
    elif low is not None and high is None:
        error = (f"please enter an integer that is"
                 f" more than / equal to {low}")

    # if the number needs to be between low & high
    else:
        error = (f"please enter an integer that"
                 f" is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()
        # check for infinite mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # check the integer is not too low
            if low is not None and response < low:
                print(error)

            # check response is more than the low number
            elif high is not None and response > high:
                print(error)

            # if response is valid, return it
            else:
                return response

        except ValueError:
            print(error)


# Main Routine goes here

# rounds = "test"
# while rounds != "":
#    rounds = int_check("Rounds <enter for infinite> ", low=1, exit_code="")
#    print(f"you asked for {rounds}")

# low_num = int_check("low Number? ")
# print(f"you chose a low number of {low_num}")

# high_num = int_check("high Number? ")
# print(f"you chose a high number of {high_num}")

# check user guesses
guess = ""
while guess != "xxx":
    guess = intcheck("guess: ", low=0, high=10, exit_code="xxx")
    print(f"you guessed {guess}")
    print()
