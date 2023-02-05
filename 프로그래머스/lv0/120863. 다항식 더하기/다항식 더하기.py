def solution(polynomial):
    exp = polynomial.split()
    x = sum([1 if e=='x' else int(e[:-1]) for e in exp if 'x' in e])
    n = sum([int(e) for e in exp if 'x' not in e and e != '+'])
    return f'{"" if x==1 else x}x + {n}' if x and n else f'{"" if x==1 else x}x' if x else f"{n}"