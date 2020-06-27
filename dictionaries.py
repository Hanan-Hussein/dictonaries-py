fruit = {"Orange": "a sweet, organge, citrus fruit",
         "apple": "good for making citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "Lime": "a sour, green citrus fruit"}
print(fruit)
print(fruit["Lime"])

# adding an entry to a dictionary
fruit["pear"] = "an odd shaped apple"
print(fruit)
fruit["pear"] = "Great with tequila"
print(fruit)
del fruit["Lime"]
print(fruit)
# fruit.clear()
# print(fruit)
while True:
    dict_key = input("Please enter a fruit :")
    if dict_key == "quit":
        break
    if dict_key in fruit:
        descrp = fruit.get(dict_key)
        print(descrp)
    else:
        print("we don't have a" + dict_key)
