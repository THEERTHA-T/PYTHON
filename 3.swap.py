#program to swap two numbers without using temporary variables

a=int(input("Enter First num :"))
b=int(input("Enter Second num :"))
print("BEFORE SWAPPING")
print("A = ",a," B = ",b)
a=a+b
b=a-b
a=a-b
print("AFTER SWAPPING")
print("A = ",a," B = ",b)
