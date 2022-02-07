# 에라토스테네스의 체를 사용해야함
# 에라토테네스의 체 : 소수 판별 알고리즘. 숫자의 제곱근 까지만 약수의 여부를 검증하는 방식

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

M, N = map(int, input().split())

for i in range(M, N + 1):
    if isPrime(i):
        print(i)


'''<시간 초괴>
m, n = map(int, input().split())

for num in range(m, n+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
'''