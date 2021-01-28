#list of vowels from a word using list comprehension

word=input("Enter a word :")
l1=[]
l1=['a','e','i','o','u']
for i in l1:
    if i in word:
        print(i)

