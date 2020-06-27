fruit = {"Orange": "a sweet, organge, citrus fruit",
         "apple": "good for making citrus fruit",
         "Lemon": "a sour citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "Lime": "a sour, green citrus fruit"}
veg = {"cabbage": "every child's favourite",
       "sprouts": "mmm lovely",
       "Spinach": "Can i have more fruit please"}
print(veg)
# veg.update(fruit)
# print(veg)
nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)