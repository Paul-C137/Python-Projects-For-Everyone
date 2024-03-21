###########################################################
# Example #1 Without a function.                          #
###########################################################
age = int(input('How old are you? '))
if age >= 21:
    print('Access Granted...')
else:
    print('Access Denied...')

###########################################################
# Example #2 With a main runtime function.                #
###########################################################
def main():
    age = int(input('How old are you? '))
    if age >= 21:
        print('Access Granted...')
    else:
        print('Access Denied...')

main()


###########################################################
# Example #3 Function performs the print action           #
###########################################################
def verify_age(age):
    if age >= 21:
        print('Access Granted...')
    else:
        print('Access Denied...')

def main():
    age = int(input('How old are you? '))
    verify_age(age)

main()

###########################################################
# Example #4 Function returns true or false and the main  #
# runtime function does the printing.                     #
###########################################################
def verify_age(age):
    if age >= 21:
        return True
    else:
        return False

def main():
    age = int(input('How old are you? '))
    if verify_age(age):
        print('Access Granted...')
    else:
        print('Access Denied...')

main()