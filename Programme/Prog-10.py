#write a python programme to print duplicates present in list

l = ["hello",20,30,40,50,50,30,90]
n = len(l)
d = []

for i in range(n):
   for j in range(i+1,n):
      if l[i]==l[j] and l[i] not in d:
             d.append(l[i])
print("Duplicates in the list are:",d)             