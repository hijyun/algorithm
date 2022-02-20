def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True, key=lambda x: x*3) # 아스키 값으로 변환되어 정렬됨
    answer = ''.join(numbers)

    return str(int(answer)) # 0인 경우 join 하면 000이런식으로 나올 수 있어서 int한 후 다시 str