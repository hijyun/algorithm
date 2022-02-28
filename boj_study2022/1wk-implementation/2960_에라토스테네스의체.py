n, k = map(int, input().split())

check = [0] * (n+1)
cnt  = 0
naljibreak = False
for i in range(2, n + 1):
    for j in range(1, n + 1, i):
        if not check[j]:
            check[j] = True
            cnt += 1

            if cnt == k:
                print(j)
                naljibreak = True
                break
    if naljibreak:
        break


