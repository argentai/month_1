for i in range (-100,100,7):
	if i%2==1:
		print(i)
a=[x>0 for x in range (-100,100)if (x%13)**2]
print (len(a))
b=[x for x in range (-100,100,7) if x%2==1]
print  (len(b))
