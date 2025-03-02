import random

SIDES = [
    'Melee Attack',
    'Melee Attack',
    'Melee Defence',
    'Ranged Attack',
    'Ranged Defence',
    'Influence'
]

def roll(sides=SIDES):
    """
    Rolls the dice and returns the result. If the result is not 'Melee Attack',
    there is a chance it will be prefixed with 'Golden '.

    :param sides: List of sides of the dice.
    :return: The result of the dice roll.
    """
    result = random.choice(sides)
    if result != 'Melee Attack':
        result = random.choice(['', 'Golden ']) + result
    return result

if __name__ == '__main__':
    print(roll())
