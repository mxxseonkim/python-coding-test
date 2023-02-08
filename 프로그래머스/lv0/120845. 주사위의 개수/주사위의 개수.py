def solution(box, n):
    ninbox = [b//n for b in box]
    return ninbox[0] * ninbox[1] * ninbox[2]