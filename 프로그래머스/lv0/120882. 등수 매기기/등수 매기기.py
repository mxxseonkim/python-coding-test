def solution(score):
    avg = [sum(s)/2 for s in score]
    sorted_avg = sorted(avg, reverse=True)
    rank_dict = {sorted_avg[i]: i+1 for i in reversed(range(len(avg)))}
    return [rank_dict[a] for a in avg]