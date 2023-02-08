def solution(n):
    now = 1
    fac = 1
    while fac <= n:
        now += 1
        fac *= now
        
    return now-1