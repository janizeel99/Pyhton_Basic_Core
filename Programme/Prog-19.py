#find the pair in list whose sum is equal to given number

list1 = [8,4,2,6,5,1,3,9]
n = len(list1)
k = 10

for i in range(n):
    for j in range(i+1,n):
        if (list1[i] + list1[j]) == k:
            print(f"The Pair on list whose total is same as given numbers is",list1[i], list1[j])

