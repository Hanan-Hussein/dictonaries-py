fruit = {"Orange": "a sweet, organge, citrus fruit",
         "Apple": "good for making citrus fruit",
         "Lemon": "a sour, sweet fruit growing in bunches",
         "Grape": "a small, sweet fruit growing in bunches",
         "Lime": "a sour, green citrus fruit"}
print(fruit)

fruit_keys = fruit.keys()
fruit["tomato"] = "Not nice with ice cream"

print(fruit_keys)
print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)
for snack in f_tuple:
    item, description = snack
    print(item + " is "+description)
print(dict(f_tuple))