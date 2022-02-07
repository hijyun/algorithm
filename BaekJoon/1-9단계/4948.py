sosu = [0] * (123456 * 2 + 1)

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in range(2,len(sosu)):
    if isPrime(i):
        sosu[i] = 1

while True:
    n = int(input())
    if not n:
        break
    print(sum(sosu[n+1:2*n+1]))

'''<후기>
- 처음엔 입력받은 수에 대해서 숫자를 세는 방식으로 풀었는데 시간 초과나옴.
- 가장 큰수까지 소수인지 아닌지 기억해둔 다음 입력받은 수에 대해서 세는 방식으로 바꿔서 통과됨.
'''