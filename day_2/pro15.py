a=17391
b=546
c=934
if a%17<b%17<c%16:
	print ('a little',a)
elif b%17<c%17<a%17:
	print ('b little',b)
else:
	print ('c little',c)
