def quadrado(n):
    s=0
    for i in range (1,2*n,2):
        s=i+s
    return s

def square (n):
    if n==1:
        return 1
    else:
        return square(n-1)+(2*n-1)
def soma (n):
    if n==1:
        return 1
    else:
        return (soma(n-1)+n)
def fib (n):
    if n==0 :
        return 0
    elif n==1:
        return 1
    else:
        return (fib(n-1) + fib(n-2))
def digitos(n,i=0):
    if n==0:
        return i
    else:
        i+=1
        return(digitos(n//10,i))
