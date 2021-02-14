class rectangle:
    def __init__(self,l,b):
        self.__l=l
        self.__b=b
        self.area=self.__l*self.__b
    def __lt__(self,a):
        if self.area<a.area:
            print("Area =",a.area)
            print("Area 2 is greater")
        else:
            print("Area =",self.area)
            print("Area 1 is greater")

l1=int(input("Enter Length of Rectangle 1:"))
b1=int(input("Enter Breadth of Rectangle 1:"))
r1=rectangle(l1,b1)

l2=int(input("Enter Length of Rectangle 2:"))
b2=int(input("Enter Breadth of Rectangle 2:"))
r2=rectangle(l2,b2)

r1<r2
