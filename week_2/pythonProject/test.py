import random
# Возьмите список имён из задания №2 и
Group = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar",
         "Bolotbek", "Alymbek", "Dastan", "Maksat"]
#
# сформируйте 4 разные команды из всех участников.
red_com = []
blue_com = []
black_com = []
silver_com = []
comandred = 'Красная команда'
comandblack = 'Черная команда'
comandsilver = 'Команда серебра'
comandblue = 'Команда синих'

i = 0
while i < 3;
    random = random.choice(Group)
    if random not in