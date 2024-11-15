s = 0

def soma(n,s):
    if n == 0:
        return s
    s += n
    
    print(s)
    return soma(n-1,s)

soma(10,s)


