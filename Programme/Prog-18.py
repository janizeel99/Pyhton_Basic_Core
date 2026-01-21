#sort a dictionary by key and that aftre value is automatically chnaged with key beacause is key value pairs.both in ascending order

dict1 = {111:"Zeel",332:"Jani",101:"Kalpesh",1:"Soma",243:"Niru",78:"Rudraa",122:"Bina"}

d = sorted(dict1.keys())
dict2 = {}

for i in d:
    dict2[i] = dict1[i]
print("Sorted Dictionary is:",dict2)    