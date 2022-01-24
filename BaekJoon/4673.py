def d(n):
    asum = 0
    for i in str(n):
        asum += int(i)
    n = n + asum
    return n


arr = set()
for i in range(10000):
    arr.add(d(i))
    if i not in arr:
        print(i)

