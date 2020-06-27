fruit = {"Orange": "a sweet, organge, citrus fruit",
         "Apple": "good for making citrus fruit",
         "Lemon": "a sour, sweet fruit growing in bunches",
         "Grape": "a small, sweet fruit growing in bunches",
         "Lime": "a sour, green citrus fruit"}
print(fruit)
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
ordered_keys = sorted(list(fruit.keys()))
for f in ordered_keys:
    print(f + " - "+fruit[f])
# the above is same as
#for f in sorted(fruits.keys()):
    #print(f+ " - "+fruit[f])

#adding an item
fruit_keys = fruit.keys()
fruit["tomato"] = "Not nice with ice cream"
print(fruit_keys)
print(fruit.items())