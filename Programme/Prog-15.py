#write a  rpogramme cto check a string is palindrome or not

data = input("Enter A Word: ")
reverse_data = data[::-1]

if reverse_data == data:
    print(f"The word {data} is a palindrome")
else:
    print(f"The word {data} is not a palindrome")    




#alag che aane lagto nathi

# name  = ["Zeel","Amit","Ravi","Kiran","Zeel","Rudraa","Rudraa"]
# duplicates = []

# for i in range(len(name)):
#     for j in range(i+1,len(name)):
#         if name[i] == name[j] and name[i] not in duplicates:
#              duplicates.append(name[i])
# print("Duplicates in the list are:",duplicates)             