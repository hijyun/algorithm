def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True, key=lambda x: (x*4)[:4]) # 아스키 값으로 변환되어 정렬됨
    if numbers[0] == '0':
    	answer = '0'
    else:
    	answer = ''.join(numbers)

    return answer