
countries_of_east = ['Singapore', 'Malaysia', 'Indonesia', 'Hawaii'] 
countries_of_central_asia = ['Kyrgyzstan', 'Kazakhstan', 'Tajikistan', 'Uzbekistan']
countries_of_europe = ['Italy', 'France', 'Germany', 'Switzerland', 'Ireland']
countries_of_america = ['Mexico', 'USA', 'Brazil', 'Columbia', 'Canada']
classes = ['Business', 'Middle', 'Econom']
#Так получилось что не все рейсы доступны всегда.
 
#Представьте что есть переменные:
user_order_0 = 'Kazakhstan'
user_order_1 = 'Madagaskar'
user_order_2 = 'Canada'
user_order_3 = 'Italy'
user_order_4 = 'Argentina'
user_order_5 = 'Malasia'
user_order_6 = 'Germany'

# Классы самолета
class_0 = {'Business': ['Germany','germany','Tajikistan','tajikistan','Hawaii','hawaii','Canada','canada']}
class_1 = {'Middle': ['Malaysia', 'Indonesia', 'Kyrgyzstan','Uzbekistan','Italy', 'France','Ireland','Mexico', 'USA', 'Brazil',]}
class_2 = {'Econom': ['Kazakhstan','kazakhstan','Switzerland','switzerland','Singapore','singapore','Colombia','colombia']}



if user_order_0 in  class_0["Business"]:
	print ("Ваш рейс найден! Ваш класс Business")

elif user_order_0 in class_2["Econom"]:
	print ("Ваш рейс найден! Ваш класс Econom")

else:
	print ("Простите рейсов в эту страну пока нет...")

while True:
	if user_order_1 in class_0["Business"]:
                print ("Ваш рейс найден! Ваш класс Business")
                break
	elif user_order_1 in class_2["Econom"]:
                print ("Ваш рейс найден! Ваш класс Econom")
                break
	else: 
                print ("Простите рейсов в эту страну пока нет...")
                break
while True:
	if user_order_2 in class_0["Business"]:
                print ("Ваш рейс найден! Ваш класс Business")
                break
	elif user_order_2 in class_2["Econom"]:
                print ("Ваш рейс найден! Ваш класс Econom")
                break
	else: 
                print ("Простите рейсов в эту страну пока нет...")
                break


while True:
	if user_order_3 in class_0["Business"]:
                print ("Ваш рейс найден! Ваш класс Business")
                break
	elif user_order_3 in class_2["Econom"]:
                print ("Ваш рейс найден! Ваш класс Econom")
                break
	else: 
                print ("Простите рейсов в эту страну пока нет...")
                break
while True:
	if user_order_4 in class_0["Business"]:
                print ("Ваш рейс найден! Ваш класс Business")
                break
	elif user_order_4 in class_2["Econom"]:
                print ("Ваш рейс найден! Ваш класс Econom")
                break
	else: 
                print ("Простите рейсов в эту страну пока нет...")
                break


while True:
	if user_order_5 in class_0["Business"]:
                print ("Ваш рейс найден! Ваш класс Business")
                break
	elif user_order_5 in class_2["Econom"]:
                print ("Ваш рейс найден! Ваш класс Econom")
                break
	else: 
                print ("Простите рейсов в эту страну пока нет...")
                break

if user_order_6 in class_0["Business"]:
	print ("Ваш рейс найден! Ваш класс Business")

elif user_order_6 in class_2["Econom"]:
	print ("Ваш рейс найден! Ваш класс Econom")

else: 
	print ("Простите рейсов в эту страну пока нет...")




# каждая из этих переменных - заказ пользователя который хочет полететь в указанную страну.

# Так как вы серьёзная компания, у вас имеется ряд правил:

# 1. Если у вас не нашлось билета в страну куда хочет клиент, вы ему вежливо говорите: "Простите рейсов в эту страну пока нет..."
# 2. Бизнес класс достxупен только для следующих стран: Germany, Tajikistan, Hawaii, Canada
# 3. Эконом класс доступен только для следующих стран: Kazakhstan, Switzerland, Singapore, Columbia
# 4. Если у вас имеется билет в эту страну - вы пишите пользователю следующее:
#        "Ваш рейс найден! Ваш класс {здесь имя класса}".
# 5. Если для этого рейса есть особый класс(Бизнес или Эконом) вы выводите именно его иначе по умолчанию стоит "Middle"
############################################################################
