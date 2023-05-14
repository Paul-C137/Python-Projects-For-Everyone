#!/usr/bin/python3

def main():
    # target number hardcoded for now
    target = 7
    # establish how many tries the user gets
    max_attempts = 3
    # this evaluates to true and sets up an infinite loop
    while True:
        # get a guess from the user
        guess = int(input("Enter a number from 1 - 10: >>> "))
        # if the guess is correct, tell the user and break out of the loop
        if guess == target:
            print("Lucky guess!")
            break
        # if you are here, the guess was not correct
        # now check if there are any tries left
        elif max_attempts > 1:
            print("Sorry, try again.")
            # decrement the number of attempts
            max_attempts = max_attempts - 1
        else:
            # if you make it this far in the if logic, the game is over
            print("Game over, man!")
            break

if __name__ == "__main__":
    main()