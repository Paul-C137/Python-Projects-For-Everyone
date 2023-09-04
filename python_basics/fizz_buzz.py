#!/user/bin/python3

'''One solution to the fizz-buzz game.'''

for number in range(1, 21):
    if number % 15 == 0:
        print('Fizz-Buzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)