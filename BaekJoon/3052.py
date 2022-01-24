# 풀이 1
arr = []
for i in range(10):
    if i == 0:
        arr.append(int(input()) % 42)
    else:
        tmp = int(input()) % 42
        if tmp not in arr:
            arr.append(tmp)
print(len(arr))

# 풀이 2
arr = []

for _ in range(10):
    n = int(input()) % 42
    arr.append(n)

print(len(set(arr)))
