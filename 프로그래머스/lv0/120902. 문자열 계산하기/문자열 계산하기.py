def solution(string):
    exp = string.split()
    answer = int(exp[0])
    
    for idx in range(1, len(exp), 2):
        op = exp[idx]
        num = int(exp[idx+1])
        answer = answer + num if op == '+' else answer - num
    
    return answer