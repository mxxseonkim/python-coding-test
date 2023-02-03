def solution(n):
    count = 0
    i = 0
    
    for i in range(1, 1000):
        if '3' not in str(i) and i % 3:
            count += 1
            
        if count == n:
            break
        
    return i