def solution(s):
    answer = [ch for ch in s if s.count(ch) == 1]    
    return ''.join(sorted(answer))