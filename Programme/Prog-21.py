#write a programme to remove pancuation from a string

str1 = "/* apples are found only | red ,green"
s = ""

for i in str1:
    if((i>= 'A' and i<='Z') | (i>='a' and i<='z' )| (i==' ')):
        s = s + i
print(s)        




num = "7,0^16741*600"
new_num_without_pancuation = ""
puncuation = ""

for i in num:
    if ((i>= '0' and i<= '9')):
        new_num_without_pancuation = new_num_without_pancuation + i
    if((i == ',') | (i == '^') | (i == '*')):
        puncuation = puncuation + i    
print(new_num_without_pancuation)
print(puncuation)