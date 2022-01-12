import random
names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek",
         'Dastan', "Maksat"]

new_list = []
i = 0
while True:
    rand_name = random.choice(names)
    if rand_name not in new_list:
        new_list.append(rand_name)
        i += 1
    if i == 4:
        break

print(new_list)
