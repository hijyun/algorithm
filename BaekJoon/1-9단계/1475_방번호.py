n = list(input())
cnt = [0] * 10
for i in n:
    idx = int(i)
    if idx == 9: # 9는 다 6으로 바꿔버림
        idx = 6
    cnt[idx] += 1

cnt[6] = (cnt[6] + 1) // 2 # 6에 저장된 숫자를 2로 나눈 것보다 가장 큰 정수

print(max(cnt))