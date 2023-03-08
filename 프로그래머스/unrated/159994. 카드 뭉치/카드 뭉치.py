def solution(cards1, cards2, goal):
    goal1 = [card for card in goal if card in cards1]
    same1 = all([True if g == c else False for g, c in zip(goal1, cards1)])
    
    goal2 = [card for card in goal if card in cards2]
    same2 = all([True if g == c else False for g, c in zip(goal2, cards2)])
    
    return "Yes" if same1 and same2 else "No"