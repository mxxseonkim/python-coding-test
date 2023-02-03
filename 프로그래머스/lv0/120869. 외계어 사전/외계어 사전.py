def solution(spell, dic):
    for word in dic:        
        if set(word) == set(spell):
            return 1
    return 2