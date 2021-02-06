#gcd of two num

n1=int(input("Enter Number 1 :"))
n2=int(input("Enter Number 2 :"))
if(n1==0 and n2==0):
    gcd=0
i=1
while(i<=n1 and i<=n2):
    if(n1%i==0 and n2%i==0):
        gcd=i
    i=i+1
print("GCD OF ",n1,"AND ",n2,"IS ",gcd)
