import random
import types
from god_favors import *
from players import Player
import tkinter as tk


# langskip = tk.Tk()

# Hrafn = tk.Frame()
# Hrafn.pack()

# bardagi = tk.Frame()
# bardagi.pack()

# valhala = tk.Label(text="How many will go to Valhalla today?")
# valhala.pack()

# beserkers = tk.Entry(width=5)
# beserkers.pack()

# skol = tk.Button(text="skol!")
# skol.pack()

# langskip.mainloop()



class Orlog:
    def __init__(self):

        player_names = [
            'Ragnar Lothbrok', 'Ivar the Boneless', 'Eric The Red',
            'Bjorn Ironside', 'Leif Erikson', 'Lagertha', 'Sigurd Snake in the Eye',
            'Ubbe Ragnarsson','Hvitserk Ragnarsson'
        ]

        prompts_get_players = [
            "How many will go to Valhalla? ",
            "Valhalla demands souls!\n",
            "Valhalla demands more souls!\n",
            "Valhalla won't accept stupid people! Say a integer number!\n",
            "Valhalla won't accept so many!\n",
        ]

        prompts_choose_gods = [
            "Which god will aid you in battle? ",
            "Which god will answer to your prayers? ",
            "Which god will give you divine gifts? ",
            "Choose an available god! "
        ]

        while \
            not (number_of_players := input(prompts_get_players[0])).isdigit() \
            or int(number_of_players) > len(player_names) \
            or int(number_of_players) <= 2 \
        :
            if number_of_players.isdigit():
                if int(number_of_players) == 0:
                    print(prompts_get_players[1])
                elif int(number_of_players) == 1:
                    print(prompts_get_players[2])
                elif int(number_of_players) < 0:
                    print(prompts_get_players[3])
                else:
                    print(prompts_get_players[4])
            else:
                    print(prompts_get_players[3])

        number_of_players = int(number_of_players)
        self.players = [
            Player(player_names.pop(random.randrange(len(player_names))))
            for _ in range(number_of_players)
        ]

        # Talvez só precise do self.order_player e não do self.players
        print([player.name for player in self.players],'\n')
        random.shuffle(self.players)
        print([player.name for player in self.players],'\n')
        gods_to_choose = dict_gods
        for prompt in prompts_choose_gods[:3]:
            for player in self.players:
                print(player)
                print(available_gods := list(gods_to_choose.keys()))
                while (chosen_god := input(prompt)) not in available_gods:
                    chosen_god = input(prompts_choose_gods[3])
                self.players[player].gods_worshipped[chosen_god] = gods_to_choose[chosen_god]
                gods_to_choose.pop(chosen_god)
                print('')

    # def roll_phase(self):



    # def god_favor_phase():

    # def resolution_phase():

    # def final_phase():

if __name__ == "__main__":
    game_orlog = Orlog()
    print('')
# Determinar a ordem dos jogadores, pode ser a mesma da escolha dos deuses para aproveitar.