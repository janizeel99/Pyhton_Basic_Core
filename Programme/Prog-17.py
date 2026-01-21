#Sort A List Without Using A Sort Keyword

list1 = [10,24,56,2,67,45,87,35]
n = len(list1)

for i in range(n):
    for j in range(i+1,n):
        if list1[i] > list1[j]:
            list1[i],list1[j] = list1[j],list1[i]

print("Sorted List is:",list1)