
def solution():
    N = int(input())
    n  = 0
    for h in range(N+1):
        for m in range(60):
            for s in range(60):
                if '3' in str(h)+str(m)+str(s):
                    n += 1
    print(n)

solution()