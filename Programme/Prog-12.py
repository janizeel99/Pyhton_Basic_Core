#rite a programme to count number of vowels in a user input name
Name = input("Enter Your Name: ")
count = 0
list_of_vowels = ['a','e','i','o','u','A','E','I','O','U']

for char in Name:
    if char in list_of_vowels:
        count += 1
print("Number of Vowels in your name is:", count)        