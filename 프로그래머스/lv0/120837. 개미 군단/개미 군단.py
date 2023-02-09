def solution(hp):
    answer = 0
    for attack in [5, 3, 1]:
        while attack <= hp:
            hp -= attack
            answer += 1
    return answer