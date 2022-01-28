n = int(input())
cnt = 0
sum = 0

while n > sum:
    cnt += 1
    sum += cnt
gap = sum - n
if cnt % 2 == 0:
    top = cnt-gap
    under = gap + 1
else:
    top = gap + 1
    under = cnt - gap
print(f'{top}/{under}')