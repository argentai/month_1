import sys
a = input('please write someting about yourself:' )
b = input('tell me your job experience in microsoft company ')
print (sys.getsizeof(a))
print (sys.getsizeof(b))
if a > b :
    print('первое занимает больше памяти')
else:
    print('второе занимает больше памяти')




