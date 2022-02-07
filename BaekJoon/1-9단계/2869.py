import math
a, b, v = map(int, input().split())
remain = (v-a)/(a-b) + 1
print(math.ceil(remain))

# 더 나은 풀이
import math
a, b, v = map(int, input().split())
remain = (v-b)/(a-b)
print(math.ceil(remain))
