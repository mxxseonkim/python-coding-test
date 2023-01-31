def solution(s1, s2):
    a = len(set(s1) - set(s2))
    return len(s1) - a