def _is_prime(numbers):
    for i in range(2, numbers):
        if numbers % i == 0: return False
    return True


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for i in numbers:
    if i == 1: continue
    if _is_prime(i): primes.append(i)
    else: not_primes.append(i)

print(f'primes: {primes}\nnot primes: {not_primes}')