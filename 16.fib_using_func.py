#fibonacci of a number

def fib(num):
    a=0
    b=1
    for i in range(1,num+1):
        print(a)
        c=a+b
        a=b
        b=c    
f=int(input("Enter a number:"))
print("FIBONACCI SERIES OF ",f,"IS")
fib(f)
