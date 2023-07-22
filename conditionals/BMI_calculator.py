#!usr/bin/python3

'''This program calculates your Body Mass Index.'''

def bmi_calc(a, b):
    bmi = a/(b**2)*703
    return bmi

def main():
    height = float(input('Enter your height in inches. >> '))
    weight = float(input('Enter you weight in pounds. >> '))
    bmi = bmi_calc(weight, height)
    print(bmi)
    if bmi < 18.5:
        print('You are underweight.')
    elif bmi < 25:
        print('You are normal weight.')
    elif bmi < 30:
        print('You are overweight.')
    elif bmi < 35:
        print('You are obese.')
    else:
        print('You are clinically obese.')

if __name__ == '__main__':
    main()