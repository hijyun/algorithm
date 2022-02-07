import sys
c = int(input())

for _ in range(c):
    score = list(map(int, sys.stdin.readline().split()))
    avg = sum(score[1:]) / score[0]
    cnt = 0

    for i in score[1:]:
        if i > avg:
            cnt += 1

    print(f'{cnt/score[0] * 100:.3f}%')