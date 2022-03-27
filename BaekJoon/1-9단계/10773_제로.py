k = int(input())
stack = []

for _ in range(k):
    n = int(input())
    if not n:
        stack.pop()
    else:
        stack.append(n)
print(sum(stack))