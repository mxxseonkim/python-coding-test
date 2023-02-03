def solution(lines):
    dup = []
    lines.sort()
    for now_idx, [now_start, now_end] in enumerate(lines):
        for start, end in lines[now_idx+1:]:
            if now_end <= start: break
            dup.append([start, now_end if now_end < end else end])
    
    if not dup: return 0
    
    dup2 = [dup[0]]
    for start, end in dup[1:]:
        if start < dup2[-1][1]:            
            dup2[-1][1] = dup2[-1][1] if end < dup2[-1][1] else end
        else:
            dup2.append([start, end])
        print(start, end, dup2)
            
    return sum(e-s for s, e in dup2)