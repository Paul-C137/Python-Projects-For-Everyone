

def is_all_letters(string):
    for char in string:
        if not char.isalpha():
            return False
    return True

def main():
    user_input = input('Type a string: >>  ')
    print(is_all_letters(user_input))

main()
