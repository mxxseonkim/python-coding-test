from collections import Counter
def solution(array):
    counter = Counter(array).most_common()
    if len(counter) == 1 or counter[0][1] != counter[1][1]:
        return counter[0][0]
    else:
        return -1