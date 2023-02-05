def solution(my_string):
    import re
    num = re.split('[a-zA-Z]+', my_string)
    return sum([int(n) for n in num if n])