#merging two dict

num1=int(input("Enter number of elements in Dictionary 1:"))
key1=[]
value1=[]
dict1={}
for i in range(num1):
    key1.append(input("Enter the key :"))
    value1.append(input("Enter the  value :"))
for i in range(num1):
    dict1.update({key1[i]:value1[i]})

num2=int(input("Enter number of elements in Dictionary 2:"))
key2=[]
value2=[]
dict2={}
for i in range(num2):
    key2.append(input("Enter the key :"))
    value2.append(input("Enter the  value :"))
for i in range(num2):
    dict2.update({key2[i]:value2[i]})
    
print("DICTIONARY 1 = ",dict1)
print("DICTIONARY 2 = ",dict2)
dict1.update(dict2)
print("MERGED DICTIONARY = ",dict1)
