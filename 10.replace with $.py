#replacing first letter repeation by $

str=input("Enter a string :")
char=str[0]
print("ACTUAL STRING : ",str)
str=str.replace(char,'$')
str1=char+str[1:]
print("MODIFIED STRING :",str1)
