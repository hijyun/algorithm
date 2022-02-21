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


# insert와 remove는 최대 O(n)의 시간복잡도를 가지고 있음
# 이를 n번 반복하니 이 풀이는 최악의 경우 O(N2)의 시간복잡도를 가질 수 있음
# 정확성도 떨어짐