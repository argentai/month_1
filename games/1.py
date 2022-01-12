import random as rd
random_number = rd.randint(0,10)

guess = 0

while guess < 3:
    my_number = input("Введите число: ")
    if  my_number.isdigit():
        my_number = int(my_number)
        if my_number < random_number:
            print("Число меньше загаданного!")
        elif my_number > random_number:
            print ("Число больше загаданного!")
        else:
            print (f"Вы угадали число - {my_number}!")
            break
        guess += 1
    else:
        print("Введено не число")
else:
    print(f"Число: {random_number} так и не было угадано!")



