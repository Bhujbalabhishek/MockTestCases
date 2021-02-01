from random import randint


def get_number():
    number = randint(1, 100)

    if number % 2 == 0:
        return 'Even number: {}'.format(number)
    else:
        return 'Odd number: {}'.format(number)