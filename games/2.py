import sys
while True:
    symbol = int(input('vvvvvvv '))
    print(sys.getsizeof(symbol))
    if symbol == 0:
        break