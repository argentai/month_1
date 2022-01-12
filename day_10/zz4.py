words = ['Anna', 'Civic', 'Kayak', 'Level', 'Madam', 'Mom', 'Noon', 'Racecar', 'Radar', 'еще', 'кабак', 'шалаш', 'лишил','language', 'which', 'means', 'vendor', 'слова', 'фраза', 'введите', 'слово', 'кнопку',]
for i in words:
    if i.lower() == i [::-1].lower():
        print (i,"Это слово полиндром ")
    else:
        print (i, "Это слово не полиндром")
