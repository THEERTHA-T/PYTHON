#area of square,rectangle,triangle using lambda function

def choice():
    print("\nMENU\n1.AREA OF SQUARE\n2.AREA OF RECTANGLE\n3.AREA OF TRIANGLE\n4.EXIT")
    ch=int(input("\nEnter your choice :"))
    if ch==1:
        side=int(input("Enter a Side :"))
        area=lambda side:side*side
        print("AREA OF SQUARE =",area(side))
        choice()
    elif ch==2:
        length=int(input("Enter Length :"))
        breadth=int(input("Enter Breadth :"))
        area=lambda l,b:length*breadth
        print("AREA OF RECTANGLE =",area(length,breadth))
        choice()
    elif ch==3:
        breadth=int(input("Enter Breadth :"))
        height=int(input("Enter Height :"))
        area=lambda b,h:((1/2)*(breadth*height))
        print("AREA OF TRIANGLE =",area(breadth,height))
        choice()
    elif ch==4:
        print("EXITING")
        return 0
    else:
        print("INVALID OPTION")
        choice()
choice()
