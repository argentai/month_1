a = input()
if len(a) > 10:
        print("vasha stroka bolshe 10 simvolov")
else:
        for i in range(len(a), 10):
                a += "*"
        print (a)