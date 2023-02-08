def solution(numbers, k):
    idx = 2 * (k-1)
    return numbers[idx % len(numbers)]