def spam(divideBy):
    return 42/divideBy

try:
    print(spam(2))
    print(spam(9))
    print(spam(5))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error, invalid argument')