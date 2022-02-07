N = int(input())
m = 2
while N != 1:
    if N % m == 0:
        print(m)
        N = N // m
    else:
        m += 1

'''<시간 초과>
n = int(input())
num = 1

while n >= num:
    num += 1
    error = 0
    for i in range(2, num):
        if num % i == 0:
            error += 1
            break
    if error == 0:
        while True:
            remain = n % num
            if not remain:
                n = n // num
                print(num)
            else:
                break
'''