n = int(input())
x, y = 1, 1
plan = input().split()

dirx = {'U' : -1, 'D' : 1, 'L' : 0, 'R' :0}

diry = {'U' : 0, 'D' : 0,'L' : -1, 'R' : 1}

for p in plan:
    tmp_x = x + dirx[p]
    tmp_y = y + diry[p]


    if tmp_x <1 or tmp_y <1 or tmp_x > n or tmp_y >n:
        continue
    x, y = tmp_x, tmp_y

print(x, y)