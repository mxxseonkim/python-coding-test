def solution(n):
    def isPrime(num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    
    return len([i for i in range(1, n+1) if not isPrime(i)])