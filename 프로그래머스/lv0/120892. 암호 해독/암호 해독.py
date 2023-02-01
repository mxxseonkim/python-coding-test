def solution(cipher, code):
    return ''.join([cipher[idx-1] for idx in range(code, len(cipher)+1, code)])