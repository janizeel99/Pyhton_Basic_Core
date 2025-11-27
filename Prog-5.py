# Sample dataset
dataset = [
    {"name": "Alice", "age": 25, "city": "Delhi"},
    {"name": "Bob", "age": None, "city": "Mumbai"},
    {"name": "Charlie", "age": 30, "city": "Delhi"},
    {"name": "David", "age": 22, "city": None}
]

num_column = "age"
cat_column = "city"


cleaned_data = []
for row in dataset:
    if all(value is not None for value in row.values()):
        cleaned_data.append(row)


total = 0
count = 0

for row in dataset:
    age = row["age"]

    try:
        age_value = float(age)
        total += age_value
        count += 1
    except:
        pass

average = total / count


category_count = {}
for row in dataset:
    category = row[cat_column]
    category_count[category] = category_count.get(category, 0) + 1


# --- Output ---
print("Cleaned Dataset:", cleaned_data)
print("Average", num_column, "=", average)
print("Category Counts for", cat_column, ":", category_count)