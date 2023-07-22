#!user/bin/python3

'''This program checks if a year is a leap year.
   There are many ways to solve this problem.  
   Can you think of a different way?'''

def leap_check_1(year):
    if year % 4 == 0: #yes
        if year % 100 == 0: #no
            if year % 400 == 0: #yes
                return True
        else:
            return True
    else:
        return False

def main():
    year = int(input('Pick a year. >> '))
    if leap_check_1(year) == True:
        print('That is a leap year')
    else:
        print('That is NOT a leap year.')

if __name__ == '__main__':
    main()  
