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