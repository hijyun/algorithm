# 풀이 1
a = int(input())
b = int(input())
c = int(input())

sum = list(map(int,list(str(a * b * c))))
arr = [0] * 10

for i in sum:
    arr[i] += 1

for a in arr:
    print(a)


# 풀이 2
A=int(input())
B=int(input())
C=int(input())
result = list(str(A*B*C))

for i in range(10):
	print(result.count(str(i)))