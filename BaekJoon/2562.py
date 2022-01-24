data = []
max_idx = 0

for i in range(9):
    data.append(int(input()))
    if data[i] > data[max_idx]:
        max_idx = i

print(data[max_idx])
print(max_idx+1)