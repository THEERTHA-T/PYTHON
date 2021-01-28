#count the occurrence of each word in a line of text

line=input("Enter the sentence :")
count=dict()
words=line.split()
for i in words:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)

