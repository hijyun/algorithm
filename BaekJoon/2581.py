m = int(input())
n = int(input())

sosu = []
sum = 0
for num in range(m, n+1):
    error = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                error += 1
                break
        if error == 0:
            sum += num
            sosu.append(num)

if sosu:
    print(sum)
    print(sosu[0])
else:
    print(-1)