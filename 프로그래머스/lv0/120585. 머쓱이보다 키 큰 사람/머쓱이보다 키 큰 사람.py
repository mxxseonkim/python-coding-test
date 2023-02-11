def solution(array, height):
    return sorted(array + [height], reverse=True).index(height)