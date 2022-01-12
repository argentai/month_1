a=float(input('enter number '))


min = a
max = a


for i in range(4):


    a=float(input('enter number '))


    if a > max:

        max = a

    if a < max and a < min:

        min = a

print('\n','min is: ',round(min,2),'\n','max is: ',round(max,2))
