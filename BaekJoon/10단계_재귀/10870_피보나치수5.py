n = int(input()) # input n

def Fibo(n):
    if n < 0:
        return False
    elif n < 2:
        return n
    else:
        return Fibo(n-1) + Fibo(n-2)

print(Fibo(n))
