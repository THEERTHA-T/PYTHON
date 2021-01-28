#ascending and descending of dictionary

d={'id':4,'name':'abc','age':22,'place':'xyz'}
print("DICTIONARY = ",d)
asc=dict(sorted(d.items()))
dsc=dict(sorted(d.items(),reverse=True))
print("ASCENDING ORDER = ",asc)
print("DESCENDING ORDER = ",dsc)
