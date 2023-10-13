import math

def isprime(n):
    if n <= 1:
        return False 

    if n <= 3:
        return True  # 2 and 3 are prime numbers

    if n % 2 == 0 or n % 3 == 0:
        return False  # Numbers divisible by 2 or 3 are not prime

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True