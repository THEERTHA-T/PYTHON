#to print positive numbers from the list

num=input("Enter list of numbers :")
list1=[]
list1=[int(i) for i in num.split()]
list2=[int(i) for i in list1 if i>0]
print("ACTUAL LIST =",list1)
print("POSITIVE NUMBERS IN LIST =",list2)
