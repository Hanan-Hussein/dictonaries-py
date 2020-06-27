farm_animals = {"Sheep", "cow", "hen"}
print(farm_animals)
for animals in farm_animals:
    print(animals)
print("-"*40)
wild_animals = set({"lion", "tiger", "panther", "elephant"})
print(wild_animals)
for animal in wild_animals:
    print(animal)
farm_animals.add("horse")
wild_animals.add("horse")
print(farm_animals)
print(wild_animals)