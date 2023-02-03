def solution(a, b):
    import math
    b = b // math.gcd(a, b)
    while b % 2 == 0: b //= 2
    while b % 5 == 0: b //= 5
    return 1 if b == 1 else 2