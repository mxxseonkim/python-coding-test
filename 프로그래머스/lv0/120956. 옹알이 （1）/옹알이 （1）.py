def solution(babbling):
    answer = 0
    
    for b in babbling:
        for w in ["aya", "ye", "woo", "ma"]:
            b = b.replace(w, ' ')
        if not b.replace(' ', ''):
            answer += 1
            
    return answer