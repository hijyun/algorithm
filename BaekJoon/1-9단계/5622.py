phone = ['ABC','DEF',' GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
chars= input()
result = 0

for char in chars:
    for i, n in enumerate(phone):
        if char in n:
            result += i
            result += 3
print(result)