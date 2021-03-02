import math


def out(n):
    if n > 10:
        return 500
    return n * math.sqrt(1 + out(n + 1))


print(out(1))