from battle_dice import SIDES, roll

class Player:
    def __init__(self, name, health_stones=15, god_favor_tokens=0, number_of_dices=6):
        self.name = name
        self.health_stones = health_stones
        self.god_favor_tokens = god_favor_tokens
        self.number_of_dices = number_of_dices
        self.gods_worshipped = {}

    def player_rolls(self, rerolls=2):
        """
        Simulates rolling dice with a specified number of rerolls.

        :param rerolls: Number of times the player can reroll the dice.
        :return: Final result of the dice rolls.
        """
        result = [roll() for _ in range(self.number_of_dices)]
        print(result)

        while rerolls > 0:
            roll_again = input(
                "Which dices do you want to roll again?\n"
                "Enter the dice indexes separated by spaces (or press Enter to keep current rolls): "
            )

            if not roll_again:
                return result

            try:
                roll_again_indexes = list(map(int, roll_again.split()))
            except ValueError:
                print("Invalid input. Please enter valid indexes.")
                continue

            if any(index < 0 or index >= self.number_of_dices for index in roll_again_indexes):
                print("One or more indexes are out of range. Please enter valid indexes.")
                continue

            for index in roll_again_indexes:
                result[index] = roll()

            rerolls -= 1
            print(result)

        return result

if __name__ == '__main__':
    euzebio = Player()
    euzebio.player_rolls()