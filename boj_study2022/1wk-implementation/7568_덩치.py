n = int(input())
people = [tuple(map(int, input().split())) for _ in range(n)]

for x, y in people:
    rank = 1
    for a, b in people:
        if x < a and y < b:
            rank += 1
    print(rank, end = ' ')