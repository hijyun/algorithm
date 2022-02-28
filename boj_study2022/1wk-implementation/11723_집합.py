import sys
m = int(input())
S = set()

for _ in range(m):
    tmp = sys.stdin.readline().split()

    if len(tmp) == 1:
        if tmp[0] == 'all':
            S = set([i for i in range(1, 21)])
        elif tmp[0] == 'empty':
            S = set()
    else:
        task, x = tmp[0], tmp[1]
        x = int(x)
        if task == 'add':
            S.add(x)
        elif task == 'remove':
            S.discard(x)
        elif task == 'check':
            if x in S:
                print(1)
            else:
                print(0)
        elif task == 'toggle':
            if x in S:
                S.discard(x)
            else:
                S.add(x)
