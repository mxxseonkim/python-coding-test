def solution(num_list):
    odd_even = [num % 2 for num in num_list]
    return [odd_even.count(0), odd_even.count(1)]