def solution(chicken):
    free, coupon = 0, 0
    remainder = chicken
    
    while remainder:
        now = remainder // 10
        coupon += remainder % 10
        now += coupon // 10
        coupon %= 10
        free += now
        remainder = now
        
    return free