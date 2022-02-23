def solution(n, lost, reserve):
    u = [1] * (n + 2) # 편의를 위해 처음과 끝을 1로 채워서 바운더리를 따로 채우지 않아도됨
    for i in reserve:
        u[i] += 1
    for i in lost:
        u[i] -= 1
    for i in range(1, n + 1):
        if u[i - 1] == 0 and u[i] == 2:
            u[i - 1:i + 1] = [1, 1]
        elif u[i] == 2 and u[i + 1] == 0:
            u[i:i + 2] = [1, 1]
    return len([x for x in u[1:-1] if x > 0]) # 유효한 배열의 값만 사용되도록