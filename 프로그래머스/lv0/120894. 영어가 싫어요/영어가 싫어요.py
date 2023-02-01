def solution(numbers):
    eng = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    result = numbers
    for idx in range(len(eng)):
        result = result.replace(eng[idx], str(idx))

    return int(result)