def solution(dots):
    dots.sort()
    w = abs(dots[0][0] - dots[2][0])
    h = abs(dots[0][1] - dots[1][1])
    return w * h