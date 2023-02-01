def solution(my_string, num1, num2):
    s = list(my_string)
    ch1 = s[num1]
    ch2 = s[num2]
    s[num1] = ch2
    s[num2] = ch1
    return ''.join(s)