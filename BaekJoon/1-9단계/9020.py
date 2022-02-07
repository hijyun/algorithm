from mytool.math import isPrime

t = int(input()) # test case
for _ in range(t):
    n = int(input())
    tmp = n // 2
    while tmp > 0:
        if isPrime(tmp):
            if isPrime(n - tmp):
                print(tmp, n-tmp)
                break
        tmp -= 1
