def solution(number, k):
    stack = []
    for i in number:
        while k > 0 and stack:
            if stack[-1] < i:
                stack.pop()
                k -= 1
            else:
                break
        stack.append(i)
    answer = ''.join(stack)
    return answer

'''<코드 리뷰>
반례
입력값: 9876543, 5

답: 98

출력값: 9876543

위와 같이 number가 9876543처럼 내림차순이면 pop함수가 호출되지 않는다.

- k번 숫자가 제거되지 않는 경우에 대한 처리가 필요함
- 제거되지 않은 만큼 stack을 비우거나 슬라이싱 해야함
'''
