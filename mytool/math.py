'''수학 관련 도구'''

# 소수 구하기 - 에레토스테네스의 체
def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True