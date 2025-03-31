

god_favors_levels = {
    'Odin':{
        'priority':7,
        'costs':[6,8,10],
        'effect_power':[3,4,5]
        },
    'Bragi':{
        'priority':4,
        'costs':[4,8,12],
        'effect_power':[2,3,4]
        },
    'Frigg':{
        'priority':2,
        'costs':[2,3,4],
        'effect_power':[2,3,4]
        },
    'Freya':{
        'priority':2,
        'costs':[2,4,6],
        'effect_power':[1,2,3]
        },
    'Mimir':{
        'priority':4,
        'costs':[3,5,7],
        'effect_power':[1,2,3]
        },
    'Tyr':{
        'priority':3,
        'costs':[4,6,8],
        'effect_power':[2,3,4]
        },
    'Skuld':{
        'priority':3,
        'costs':[4,6,8],
        'effect_power':[2,3,4]
        },
    'Loki':{
        'priority':2,
        'costs':[3,6,9],
        'effect_power':[1,2,3]
        },
    'Thrymr':{
        'priority':1,
        'costs':[3,6,9],
        'effect_power':[1,2,3]
        },
    'Var':{
        'priority':1,
        'costs':[10,14,18],
        'effect_power':[1,2,3]
        },
    'Heimdall':{
        'priority':4,
        'costs':[4,7,10],
        'effect_power':[1,2,3]
        },
    'Idun':{
        'priority':7,
        'costs':[4,7,10],
        'effect_power':[2,4,6]
        },
    'Brunhild':{
        'priority':4,
        'costs':[4,10,18],
        'effect_power':[1.5,2,3]
        },
    'Freyr':{
        'priority':4,
        'costs':[4,6,8],
        'effect_power':[2,3,4]
        },
    'Vidar':{
        'priority':4,
        'costs':[2,4,6],
        'effect_power':[2,4,6]
        },
    'Hel':{
        'priority':4,
        'costs':[6,12,18],
        'effect_power':[1,2,3]
        },
    'Thor':{
        'priority':6,
        'costs':[4,8,12],
        'effect_power':[2,5,8]
        },
    'Skadi':{
        'priority':4,
        'costs':[6,10,14],
        'effect_power':[1,2,3]
        },
    'Baldr':{
        'priority':4,
        'costs':[3,6,9],
        'effect_power':[1,2,3]
        },
    'Ullr':{
        'priority':4,
        'costs':[2,3,4],
        'effect_power':[2,3,6]
        },
}




# FAZER A BATALHA PRIMEIRO E DEPOIS PENSAR COMO ADICIONAR OS GOD FAVOUR.
# MAS TU JÁ COMEÇOU BEM!!!!!
# ADICIONAR OS GOD FAVOURS NOS DICTS POR ENQUANTO
# TEM MUITA INFORMAÇÃO QUE PRECISA ARMAZENAR E PASSAR EM CADA ROUND, TIPO OS DADOS E NÚMERO DE VIDA ESCOLHIDO
# TU PODE VER TODAS AS HABILIDADES E ANOTAR TUDO!!!!!!

# número de vida escolhido
# número de dados que rolaram roubar
# número de dados que rolaram flecha
# level do god favour
# número de god tokens gasto
# Número de ataques bloqueados
# Dados dos jogadores
# dano recebido
# número de dados que rolaram machado
# Maior número do mesmo tipo de dado
# Dano causado no oponente
# número de dados que rolaram capacete
# # número de dados que rolaram escudo


class god_favor:

    def __init__(self, effect, tokens_level_costs, effect_power, priority, after_resolution = False):
        self.effect = effect
        self.tokens_level_cost = tokens_level_costs
        self.effect_power = effect_power
        self.priority = priority
        self.after_resolution = after_resolution

    def activate(self, player, level, **kwargs):
        if player.god_favor_tokens >= self.tokens_lv_cost[level]:
            player.god_favor_tokens -= self.tokens_lv_cost[level]
            self.effect(level, **kwargs)
        else:
            print(f"{player.name} does not have enough god favor tokens!")


# Quando for usar os God favours, armazenar todos os dados das funções e só depois executar na ordem correta.


# Vale a pena fazer classe dos deuses, porque eles tem várias coisas em comum

def odins_sacrifice(level, player, health):
    player.health_stones -= health
    player.god_favor_tokens += god_favors_levels['Odin']['effect_power'][level-1]*health

def bragis_verve(level, player, hand_die):
    player.god_favor_tokens += god_favors_levels['Bragi']['effect_power'][level-1]*hand_die

def friggs_sight(level, player, target):
    player.dice_roll
    target.dice_roll += god_favors_levels['Frigg']['effect_power'][level-1]

def freyas_plenty(level, player,):
    player.number_of_dices += god_favors_levels['Freya']['effect_power'][level-1]

def mimirs_wisdom(level, player,damage):
    player.god_favor_tokens += god_favors_levels['Mimir']['effect_power'][level-1]*damage

def tyrs_pledge(level, player, target, health):
    player.health_stones -= health
    target.god_favor_tokens -= god_favors_levels['Tyr']['effect_power'][level-1]*health
    if target.god_favor_tokens < 0:
        target.god_favor_tokens = 0
    # TENHO QUE TOMAR CUIDADO COM NUMEROS NEGATIVOS

def skulds_charm(level, player,target, arrow):
    target.god_favor_tokens -= god_favors_levels['Skuld']['effect_power'][level-1]*arrow
    # Each die of the player or the target that rolled arrow?

def lokis_trick(level, target, dices):
    dices = input() # FAZER O INPUT BASEADO NO LEVEL
    for i in len(dices):
        target.dice_roll.pop()

def thymrs_theft(level, target, dices):
    target.god_favor_level -= god_favors_levels['Thrymr']['effect_power'][level-1]

def vars_bond(level, player, god_favor_tokens):
    player.health_stones += god_favor_tokens*god_favors_levels['Var']['effect_power'][level-1]

def heimdalls_watch(level, player, blocked_attacks):
    player.health_stones += blocked_attacks*god_favors_levels['Heimdall']['effect_power'][level-1]

def iduns_rejuvenation(level, player):
    player.health_stones += god_favors_levels['Idun']['effect_power'][level-1]

def brunhilds_fury(level, player, n_machados):
    player.dice_roll.append('Machado')*god_favors_levels['Brunhild']['effect_power'][level-1]

def freyrs_gift(level, player, maioria):
    player.dice_roll.append(maioria)*god_favors_levels['Freyr']['effect_power'][level-1]

def vidars_might(level, player, capacete):
    player.dice_roll.remove(capacete)*god_favors_levels['Vidar']['effect_power'][level-1]

def hels_grip(level, player, target_damage):
    player.health_tokens =+ target_damage*god_favors_levels['Hel']['effect_power'][level-1]

def thors_strike(level, target):
    target.health_tokens -= god_favors_levels['Thor']['effect_power'][level-1]

def skadis_hunt(level, player, arrows):
    player.dice_roll.append(arrows)*god_favors_levels['Skadi']['effect_power'][level-1]

def baldrs_invulnerability(level, player, defesa,_cap, defesa_esc):
    player.dice_roll.append(defesa)*god_favors_levels['Baldr']['effect_power'][level-1]
    player.dice_roll.append(defesa)*god_favors_levels['Baldr']['effect_power'][level-1]

def ullrs_aim(level, player, arrow_bipass, target):
    player.dice_roll.remove(arrow_bipass)*god_favors_levels['Ullr']['effect_power'][level-1]
    # Tenho que atacar com 2 flechas a mais, mas o oponente não pode perder o escudo para os ataques dos outros


print('')