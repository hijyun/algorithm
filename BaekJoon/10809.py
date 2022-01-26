# 풀이 1 - 딕셔너리 이용
abc = list('abcdefghijklmnopqrstuvwxyz')
cnt = [-1] * 26
dic = dict(zip(abc,cnt))

char = list(input())

for n in char:
    dic[n] = char.index(n)

for _, r in dic.items():
    print(r, end=' ')

# 풀이 2 - 아스키코드 이용
check = [-1] * 26
chars = input()

for i, char in enumerate(chars):
    idx = ord(char) - 97
    if check[idx] == -1:
        check[ord(char) - 97] = i
print(*check)