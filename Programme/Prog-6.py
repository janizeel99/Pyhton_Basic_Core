
def group_by_category(products):
    category_totals = {}

    for item in products:
        category = item.get("category")
        price = item.get("price", 0)

    
        if category not in category_totals:
            category_totals[category] = 0
        
    
        category_totals[category] += price

    return category_totals     


Products = [
    {'category':'Electronics','price':200},
    {'category':'Clothing','price':50},
    {'category':'Electronics','price':150},
    {'category':'Groceries','price':100},
    {'category':'Clothing','price':80},
    {'category':'Groceries','price':60}
]


result = group_by_category(Products)
print(result)