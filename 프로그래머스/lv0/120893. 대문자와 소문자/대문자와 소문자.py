def solution(my_string):
    revised = [ch.lower() if ch.isupper() else ch.upper() for ch in my_string]
    return ''.join(revised)