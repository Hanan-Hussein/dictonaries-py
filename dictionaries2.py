fruit = {"Orange": "a sweet, organge, citrus fruit",
         "apple": "good for making citrus fruit",
         "lemon": "a sour, sweet fruit growing in bunches",
         "grape": "a small, sweet fruit growing in bunches",
         "Lime": "a sour, green citrus fruit"}
print(fruit)
for i in range(10):

    for snack in fruit:
        print(snack + " is " + fruit[snack])
    print('-'*40)

