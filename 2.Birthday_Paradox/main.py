import datetime, random


def get_match(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None

    for i, birthday_a in enumerate(birthdays):
        for j, birthday_b in enumerate(birthdays[i+1:]):
            if birthday_a == birthday_b:
                return birthday_a


def generate_birthdays(number_of_birthdays):
    birthdays = []
    for i in range(0, number_of_birthdays):
        start_date = datetime.date(2001, 1, 1)
        birthday = start_date + datetime.timedelta(random.randint(0, 364))
        birthdays.append(birthday)
    return birthdays

    
def start():
    print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com
  
  The birthday paradox shows us that in a group of N people, the odds
  that two of them have matching birthdays is surprisingly large.
  This program does a Monte Carlo simulation (that is, repeated random
  simulations) to explore this concept.
  
  (It's not actually a paradox, it's just a surprising result.)
  ''')

    MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    print("How many birthdays shall I generate? (Max 100)", end="\n")
    number_of_birthdays = 0
    while True:
        number_of_birthdays = input("> ")
        if number_of_birthdays.isdecimal() and 1 <= int(number_of_birthdays) <=100:
            number_of_birthdays = int(number_of_birthdays)
            break
        else :
            print('Invalid entry! Try again!')
    birthdays = generate_birthdays(number_of_birthdays)
    print('Here are {} birthdays ->'.format(number_of_birthdays))
    for birthday in birthdays:
        month_name = MONTHS[birthday.month - 1]
        date_text = '{} {}'.format(month_name, birthday.day)
        print(date_text, end=', ')
    match = get_match(birthdays)
    print('match:', match)
    if match:
        print('There are multiple people with {} {} birth date'.format(MONTHS[match.month-1], match.day))

    
    # running 100,000 simulations
    print()
    print('Running 100,000 simulations---')
    matches = 0
    for i in range(100000):
        birthdays = generate_birthdays(number_of_birthdays)
        match = get_match(birthdays)
        if match:
            matches += 1
    
    print('Out of 100,000 simulations of {} people, {} times there was a match in the sample, \n this means {} have {} % chance of having a match'.format(number_of_birthdays, matches,number_of_birthdays, round((matches/100000)*100,2)))


if __name__ == "__main__":
    start()
