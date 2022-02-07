# 단어 공부
word = input().upper()
cnt = [0] * 26

for s in word:
    cnt[ord(s)-65] += 1

max_idx = 0
for i, c in zip(range(26),cnt):
    if c > cnt[max_idx]:
        max_idx = i

if cnt.count(cnt[max_idx]) > 1:
    print('?')
else:
    print(chr(max_idx+65))