def solution(A, B):
    answer = -1
    
    for i in range(len(A)):
        now = A[-i:] + A[:-i]
        if now == B:
            answer = i
            break
    
    return answer