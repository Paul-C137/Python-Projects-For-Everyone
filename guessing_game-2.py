#Improvement:
# 1. Best practice.
# 2. Use a while loop and give them 3 chances.
# 3. Account for upper and lower case user input.
# 4. Inform user that they didn't type anything.
# 5. Add colorized output.
# 6. Remove item from list.
# 7. Move your data to a file.
# 8. Forget about your own questions and get them from an API.
# 9. Keep score.

import random

q = [
    {'United States': 'Washington DC'},
    {'Germany': 'Berlin'},
    {'France': 'Paris'}
]

choice = random.choice(q)
#print(choice)

country = list(choice.keys())[0]

guess = input(f'What is the capital of {country}?')

capital = choice[country]

if guess == capital:
    print('Hooraay!')
else:
    print('Loooooooser!')




