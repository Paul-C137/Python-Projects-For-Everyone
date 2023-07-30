#!/user/bin/python3

'''Sum all the numbers from 1 - 100 by looping across a pre-defined range.'''

# Start at 0
answer = 0
# We have to go up to but NOT including 101.  That's just how the range() 
# function works.
for i in range(1,101):
    #answer = answer + i
    answer += i
print(f'The answer is: {answer}')