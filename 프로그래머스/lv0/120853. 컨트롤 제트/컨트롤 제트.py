def solution(s):
    answer = 0
    s = s.split()
    idx = len(s)-1
    while 0 <= idx:
        if s[idx] == 'Z': idx -= 1
        else: answer += int(s[idx])
        idx -= 1
    return answer