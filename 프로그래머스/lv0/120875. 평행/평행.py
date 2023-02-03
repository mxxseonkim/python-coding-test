def solution(dots):
    
    def gradient(dot1, dot2):
        return (dot1[1] - dot2[1]) / (dot1[0] - dot2[0]) if (dot1[0] - dot2[0]) else 0
    
    if gradient(dots[0], dots[1]) == gradient(dots[2], dots[3]) or gradient(dots[0], dots[2]) == gradient(dots[1], dots[3]):
        return 1
    
    return 0