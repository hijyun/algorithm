n = int(input())

for _ in range(n):
    test = input()
    sum = 0
    score = 0

    for i in test:
        if i == 'O':
            sum += 1
            score += sum
        else:
            sum = 0

    print(score)