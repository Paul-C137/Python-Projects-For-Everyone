

def is_all_letters(string):
    for char in string:
        if not char.isalpha():
            return False
    return True

def main():
    while True:
        user_input = input('Type a string with only letters: >>  ')
        if is_all_letters(user_input):
            print('Thanks for following the instructions')
            break
        print('Please follow the instructions.')

if __name__ == "__main__":
    main()
