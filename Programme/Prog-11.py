#write a python programme to count number of item having list as values

data = {'Fruits':["apple","mango","banana"], 'Vegetables':["carrot","potato"], "Dairy":"milk", "Grains":"Rice"}

count = 0
for i in data:
    if isinstance(data[i], list):
        count += 1
print("Number of items having list as values:", count)