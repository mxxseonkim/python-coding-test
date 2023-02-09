def solution(age):
    alp = list('abcdefghij')
    return ''.join([alp[int(n)] for n in str(age)])