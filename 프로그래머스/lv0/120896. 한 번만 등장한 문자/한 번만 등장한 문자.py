def solution(s):
    answer = [ch for ch in set(s) if s.count(ch) == 1]    
    return ''.join(sorted(answer))