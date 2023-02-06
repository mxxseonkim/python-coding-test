def solution(keyinput, board):
    x, y = 0, 0
    xlimit, ylimit = [n//2 for n in board]
    for key in keyinput:
        if key=='left' and -xlimit<x: x-=1
        elif key=='right' and x<xlimit: x+=1
        elif key=='down' and -ylimit<y: y-=1
        elif key=='up' and y<ylimit: y+=1
    return [x, y]