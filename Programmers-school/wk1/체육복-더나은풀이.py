def solution(n, lost, reserve):
    answer = 0

    cloth_counts = [1] * 32

    for l in lost:
        cloth_counts[l] -= 1
    for r in reserve:
        cloth_counts[r] += 1

    for i in range(1, 31):
        cloth_count = cloth_counts[i]
        if cloth_count == 2:
            if not cloth_counts[i - 1]:
                cloth_counts[i - 1] += 1
                cloth_counts[i] -= 1
            elif not cloth_counts[i + 1]:
                cloth_counts[i + 1] += 1
                cloth_counts[i] -= 1

    for i in range(1, n + 1):
        if cloth_counts[i] > 0:
            answer += 1

    return answer