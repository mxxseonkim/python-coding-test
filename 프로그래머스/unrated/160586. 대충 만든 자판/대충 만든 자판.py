def solution(keymap, targets):
    ch = list(set(''.join(targets)))
    cnts = [[k.find(c) for k in keymap if c in k] for c in ch]
    cnt = [min(c)+1 if c else 0 for c in cnts]
    dic = dict(zip(ch, cnt))
    
    answer = []
    for target in targets:
        answer.append(0)
        for t in list(target):
            if dic[t] == 0:
                answer[-1] = -1
                break
            answer[-1] += dic[t]
    
    return answer