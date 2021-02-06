#pyramid of a number

def pyramid(p):
    for i in range(1,p+1):
        for j in range(1,i+1):
            print(i*j,end=" ")
        print("\n")    
p=int(input("Enter a number:"))
pyramid(p)
