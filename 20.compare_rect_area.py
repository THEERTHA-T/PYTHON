class rectangle:
    def __init__(self,l,b):
        self.len=l
        self.bred=b
    def disp_peri(self):
        print("PERIMETER =",2*(self.len+self.bred))
    def disp_area(self):
        area1=self.len*self.bred
        print("AREA =",area1)
        return area1
def rec():
    print("\nMENU\n1.AREA OF RECTANGLE\n2.PERIMETER OF RECTANGLE\n3.COMPARE AREAS OF RECTANGLE\n4.EXIT")
    c=int(input("Enter choice :"))
    if c==1:
        l=int(input("Enter Length 1:"))
        b=int(input("Enter Breadth 1:"))
        s=rectangle(l,b)
        s.disp_area()
        rec()
    elif c==2:
        l=int(input("Enter Length 2:"))
        b=int(input("Enter Breadth 2:"))
        s=rectangle(l,b)
        s.disp_peri()
        rec()
    elif c==3:
        l1=int(input("Enter Length 1:"))
        b1=int(input("Enter Breadth 1:"))
        s=rectangle(l1,b1)
        l2=int(input("Enter Length 2:"))
        b2=int(input("Enter Breadth 2:"))
        t=rectangle(l2,b2)
        if s.disp_area()>t.disp_area():
            print("Area 1 is Greater")
        else:
            print("Area 2 is Greater")
        rec()
    elif c==4:
        print("EXITING")
        return 0
    else:
        print("INVALID CHOICE")
rec()
