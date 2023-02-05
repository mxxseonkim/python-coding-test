def solution(sides):
    answer = min(sides) + (sum(sides)-max(sides)-1)
    return answer