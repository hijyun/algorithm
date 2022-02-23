def solution(n, lost, reserve):
    s = set(lost) & set(reserve)
    reserve = set(reserve) - s
    lost = set(lost) - s
    for i in reserve:
        if i - 1 in lost:
            lost.remove(i - 1)
        elif i + 1 in lost:
            lost.remove(i + 1)

    answer = n - len(lost)

    return answer