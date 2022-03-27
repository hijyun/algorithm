import sys
from collections import Counter
n = int(sys.stdin.readline())
data = []
for i in range(n):
    data.append(int(sys.stdin.readline()))

data.sort()
print(round(sum(data) / n)) # 산술 평균
print(data[n // 2]) # 중앙값

cnt = Counter(data).most_common(2) # 최빈값
if n > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(data[0])
print(data[-1] - data[0]) # 범위