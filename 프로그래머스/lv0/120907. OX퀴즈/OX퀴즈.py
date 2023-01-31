def solution(quiz):
    result = []
    for exp in quiz:
        n1, op, n2, _, n3 = exp.split()        
        if op == '+':
            r = 'O' if int(n1) + int(n2) == int(n3) else 'X'
        else:
            r = 'O' if int(n1) - int(n2) == int(n3) else 'X'
        result += r
    return result