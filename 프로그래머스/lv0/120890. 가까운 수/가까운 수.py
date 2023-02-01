def solution(array, n):
    idx = 0
    array.sort()
    
    for i in range(1, len(array)):
        d1 = abs(array[idx] - n)
        d2 = abs(array[i] - n)
        idx = idx if d1 <= d2 else i
    
    return array[idx]