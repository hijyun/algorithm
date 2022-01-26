# 문자열 반복
t = int(input())

for n in range(t):
    r, s = input().split(' ')
    for i in s:
        print(i*int(r), end='')
    print()