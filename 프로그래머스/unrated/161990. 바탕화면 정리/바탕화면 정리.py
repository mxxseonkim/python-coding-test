def solution(wallpaper):
    x, y = [], []
    
    for xi in range(len(wallpaper)):
        for yi in range(len(wallpaper[0])):
            if wallpaper[xi][yi] == '#':
                x.append(xi)
                y.append(yi)
    
    return [min(x), min(y), max(x)+1, max(y)+1]