def solution(numlist, n):
    numlist.sort(reverse=True)
    return sorted(numlist, key=lambda x: abs(n-x))