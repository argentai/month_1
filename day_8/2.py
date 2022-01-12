с = input('vvedite')
l = len(с)
l = l//2
for i in range(l):
    if с[i] != с[-1-i]:
        print("It's not palindrome")
        quit()
print("It's palindrome")

