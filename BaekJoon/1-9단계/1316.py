# 그룹 단어 체커
n = int(input())
cnt = 0
for _ in range(n):
    word = input()
    stack = []
    for char in word:
        if not stack:
            stack.append(char)
        elif char in stack:
            if stack.pop() == char:
                stack.append(char)
            else:
                stack.append(-1)
                break
        else:
            stack.append(char)
    if -1 not in stack:
        cnt += 1
print(cnt)

# 더 나은 풀이
n = int(input())

group_word = 0
for _ in range(n):
    word = input()
    error = 0
    for index in range(len(word)-1):  # 인덱스 범위 생성 : 0부터 단어개수 -1까지
        if word[index] != word[index+1]:  # 연달은 두 문자가 다른 때,
            new_word = word[index+1:]  # 현재글자 이후 문자열을 새로운 단어로 생성
            if new_word.count(word[index]) > 0:  # 남은 문자열에서 현재글자가 있있다면
                error += 1  # error에 1씩 증가.
    if error == 0:
        group_word += 1  # error가 0이면 그룹단어
print(group_word)