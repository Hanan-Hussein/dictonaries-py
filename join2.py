locations = {0: "You are sitting in front of a computer learning python",
             1: "you are standing at the end of a road before a small brick building",
             2: "you are at the top of a hill",
             3: "you are inside a building, a well house for a small stream",
             4: "you are in a valley beside a stream",
             5: "you are in the forest"}
exits =[{"Q" : 0},
        {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
        {"N": 5, "Q": 0},
        {"W": 1, "Q": 0},
        {"N": 1, "W": 2, "Q": 0},
        {"W": 2, "S": 1, "Q": 0}]
loc = 1
while True:
    availableExits = "".join(exits[loc].keys())
    # for direction in exits[loc].keys():
    #     availableExits += direction + ", "
    print(locations[loc])
    if loc == 0:
        break

    direction = input("Available exists are "+ availableExits+" ").upper()
    print()

    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cant go in that direction")
