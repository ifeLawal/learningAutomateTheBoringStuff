def spam(divideBy):
    return 42 / divideBy

try:
    print(spame(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')
