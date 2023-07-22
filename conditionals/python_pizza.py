#!user/bin/python3

'''This program calculates the final bill for a pizza order depending on the
   input from the user.'''

def calculate_bill(size, pepperoni, extra_cheese):
    if size == 's':                                                                                                                                                                                                                                                 
        bill = 15
        if pepperoni == 'y':
            bill += 2
    elif size == 'm':
        bill = 20
        if pepperoni == 'y':
            bill += 3 
    else:
        bill = 25
        if pepperoni == 'y':
            bill += 3
    if extra_cheese == 'y':
            bill += 1
    return bill

def main():
    print('Welcome to Python Pizza!')
    size = input('What size pizza would you like? (S,M,L) >> ').lower()
    add_pepperoni = input('Would you like pepperoni? (Y,N)>> ')
    add_cheese = input('Would you like extra cheese? (Y,N) >> ')
    bill = calculate_bill(size, add_pepperoni, add_cheese)
    print(f'Your final bill is: ${bill}.') 

if __name__ == '__main__':
    main()