def solution(numbers):
    from itertools import combinations
    n = [n1*n2 for n1, n2 in combinations(numbers, 2)]
    return max(n)