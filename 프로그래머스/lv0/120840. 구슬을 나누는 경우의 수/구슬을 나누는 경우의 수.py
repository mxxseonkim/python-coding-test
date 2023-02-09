def solution(balls, share):
    from math import factorial as fac
    return fac(balls) / (fac(balls-share) * fac(share))