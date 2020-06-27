locations = {0: "You are sitting in front of a computer learning python",
             1: "you are standing at the end of a road before a small brick building",
             2: "you are at the top of a hill",
             3: "you are inside a building, a well house for a small stream",
             4: "you are in a valley beside a stream",
             5: "you are in the forest"}
exits ={0: {"Q" : 0},
        1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
        2: {"N": 5, "Q": 0},
        3: {"W": 1, "Q": 0},
        4: {"N": 1, "W": 2, "Q": 0},
        5: {"W": 2, "S": 1, "Q": 0}}
vocabularies = {"QUIT": "Q",
                "NORTH": "N",
                "SOUTH": "S",
                "WEST": "W",
                "EAST": "E"}
loc = 1
while True:
    availableExits = "".join(exits[loc].keys())
    print(locations[loc])
    if loc == 0:
        break

    direction = input("Available exists are "+ availableExits + " ").upper()
    print()
    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in vocabularies:
                direction = vocabularies[word]
                break
        # for word in vocabularies:
            # if word in direction:
            #     direction = vocabularies[word]
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cant go in that direction")
