import random


def _key(n):
    print(n)
    result = []
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                result.append(i)
                result.append(j)
    return result


print(*_key(random.randrange(3, 20)), sep='')
