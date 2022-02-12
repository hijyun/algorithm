import sys
sys.setrecursionlimit(10**6)

def print_stars(n):
    if n == 1:
        return ['*']

    Stars = print_stars(n // 3)
    result = []

    for star in Stars:
        result.append(star * 3)
    for star in Stars:
        result.append(star+ ' '*(n // 3) + star)
    for star in Stars:
        result.append(star * 3)

    return result

n = int(sys.stdin.readline().strip())
print('\n'.join(print_stars(n)))




'''<어려웠던 이유>
- 칸을 9개로 나누어서 생각하려고했는데 복잡해짐
- 칸을 3개로 나누어서 재귀구조를 넣으면 쉽게 풀리는듯

'''
