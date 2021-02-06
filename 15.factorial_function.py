#calculate factorial of a number

def fact(n):
    if n<0:
        return 0
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
n=int(input("Enter a number :"))
print("FACTORIAL OF ",n,"IS ",fact(n))
