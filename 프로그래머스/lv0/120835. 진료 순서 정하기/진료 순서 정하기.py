def solution(emergency):
    sort = sorted(emergency, reverse=True)
    rank = dict([(sort[i], i+1)for i in range(len(emergency))])
    return [rank[e] for e in emergency]