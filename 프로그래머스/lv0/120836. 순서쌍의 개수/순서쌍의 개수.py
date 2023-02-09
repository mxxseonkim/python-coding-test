def solution(n):
    import math
    return len([[i, n//i] for i in range(1, n+1) if n%i == 0])