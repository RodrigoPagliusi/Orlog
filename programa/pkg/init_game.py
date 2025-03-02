import random
import types
import god_favors, players
import tkinter as tk


langskip = tk.Tk()

Hrafn = tk.Frame()
Hrafn.pack()

bardagi = tk.Frame()
bardagi.pack()

valhala = tk.Label(text="How many will go to Valhalla today?")
valhala.pack()

beserkers = tk.Entry(width=5)
beserkers.pack()

skol = tk.Button(text="skol!")
skol.pack()



langskip.mainloop()



player_names = [
    'Ragnar Lothbrok', 'Ivar the Boneless', 'Eric The Red',
    'Bjorn Ironside', 'Leif Erikson', 'Lagertha', 'Sigurd Snake in the Eye'
]

prompts_get_players = [
    "How many will go to Valhalla? ",
    "Valhalla won't accept so many! Choose less: ",
    "Choose an available god! "
]

prompts_choose_gods = [
    "Which god will aid you in battle? ",
    "Which god will answer to your prayers? ",
    "Which god will give you divine gifts? "
]

def get_players():
    number_of_players = int(input(prompts_get_players[0]))
    while number_of_players > len(player_names):
        number_of_players = int(input(prompts_get_players[1]))
    return {
        player_names.pop(random.randrange(len(player_names))): players.Player()
        for _ in range(number_of_players)
    }

def choose_gods(players):
    shuffled_players = list(players.keys())
    random.shuffle(shuffled_players)
    for prompt in prompts_choose_gods:
        for player in shuffled_players:
            print(player)
            available_gods = list(god_favors.dict_gods.keys())
            print(available_gods)
            chosen_god = input(prompt)
            while chosen_god not in available_gods:
                chosen_god = input(prompts_get_players[2])

            players[player].gods_worshipped.append(chosen_god)
            setattr(players[player],
                    god_favors.dict_gods[chosen_god].__name__,
                    types.MethodType(god_favors.dict_gods[chosen_god], players[player])
                    )
            god_favors.dict_gods.pop(chosen_god)


if __name__ == "__main__":
    dict_players = get_players()
    choose_gods(dict_players)



print(dict_players)
# Determinar a ordem dos jogadores




# cada jogador começa com 6 dados
# cada jogador começa com 15 de vida
# cada jogador escolhe 3 deuses dos 20 disponíveis