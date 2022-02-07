dicx = {}
dicy = {}
for _ in range(3):
    x, y = map(int, input().split())
    if x in dicx:
        dicx[x] += 1
    else:
        dicx[x] = 1
    if y in dicy:
        dicy[y] += 1
    else:
        dicy[y] = 1


print(sorted(dicx.items(), key=lambda x : x[1])[0][0], end=' ')
print(sorted(dicy.items(), key=lambda x : x[1])[0][0], end=' ')

'''<다른 풀이>
x_ = []
y_ = []
for i in range(3):
        x, y = map(int, input().split())
        x_.append(x)
        y_.append(y)
for i in range(3):
        if x_.count(x_[i]) == 1:
                x = x_[i]
        if y_.count(y_[i]) == 1:
                y = y_[i]
print(x, y)
'''