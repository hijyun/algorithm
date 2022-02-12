chars = input()
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
n = 0
for c in cro:
    chars = chars.replace(c, '*')

print(len(chars))