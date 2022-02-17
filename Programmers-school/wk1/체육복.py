def solution(n, lost, reserve):
    reserve = set(reserve) - set(lost)
    lost = set(lost) - set(reserve)
    for i in reserve:
        if i - 1 in lost:
            lost.remove(i - 1)
        elif i + 1 in lost:
            lost.remove(i + 1)

    answer = n - len(lost)

    return answer
