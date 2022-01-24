def solution():
    a = list(map(int,input().split()))
    sum_a = 0
    for i in a:
        sum_a += i

    return sum_a

print(solution())