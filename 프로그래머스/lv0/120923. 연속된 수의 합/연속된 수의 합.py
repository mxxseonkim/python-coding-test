def solution(num, total):
    start = total // num - num // 2
    if num % 2 == 0: start += 1
    answer = [*range(start, start + num)]
    return answer