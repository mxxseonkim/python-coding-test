def solution(rsp):
    return ''.join(['0' if n=='2' else '2' if n=='5' else '5' for n in rsp])