n=int(input('VVEDI CHISLO'))
if  n>99 and n<1000:
	print ("eto chislo trex znachnoe")
if n<100 and n>9:
	print ('eto chislo dvux znachnoe')
if n>0 and n%2==0:
	print ("polozhitelnoe i chetnoe")
if n%31==0:
	print ("delitsya bez ost")
if n>100 and n%17==0 or n>150 and n==13**2:
	print ('MAIN')
else:
	print (n)
