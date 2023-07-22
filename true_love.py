#!user/bin/python3

'''This program uses science to calculate your compatability score with your
   partner.'''

def calculate_score(name):
    point_1 = 0
    point_2 = 0
    for i in name.lower():
        if i in 'true':
            point_1 += 1
    for i in name.lower():
        if i in 'love':
            point_1 += 1
    return point_1, point_2

def main():
    print("Is it love?  There's only one way to find out!")
    your_name = (input('Please enter your first and last name. >> '))
    their_name = (input('Please enter their first and last name. >> '))
    name = your_name + their_name
    first_score, last_score = calculate_score(name)
    final_score = first_score * 10 + last_score
    if final_score >= 100:
        final_score = 100

    print(f'You two are {final_score}% compatible!')

if __name__ == '__main__':
    main()
