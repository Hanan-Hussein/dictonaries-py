locations = {0: "You are sitting in front of a computer learning python",
             1: "you are standing at the end of a road before a small brick building",
             2: "you are at the top of a hill",
             3: "you are inside a building, a well house for a small stream",
             4: "you are in a valley beside a stream",
             5: "you are in the forest"}
exits ={0: {"Q": 0},
        1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
        2: {"N": 5, "Q": 0},
        3: {"W": 1, "Q": 0},
        4: {"N": 1, "W": 2, "Q": 0},
        5: {"W": 2, "S": 1, "Q": 0}}
named_exits = {1: {"2": 2, "3": 3, "5": 5, "4": 4},
               2: {"5": 5},
               3: {"1": 1},
               4: {"1": 1, "2": 2},
               5: {"2": 2, "1": 1}}
vocabularies = {"QUIT": "Q",
                "NORTH": "N",
                "SOUTH": "S",
                "WEST": "W",
                "EAST": "E",
                "ROAD": "1",
                "HILL": "2",
                "BUILDING": "3",
                "VALLEY": "4",
                "FOREST": "5"}
loc = 1
while True:
    availableExits = "".join(exits[loc].keys())
    print(locations[loc])
    if loc == 0:
        break
    else:
        all_exits = exits[loc].copy()
        all_exits.update(named_exits[loc])

    direction = input("Available exists are "+ availableExits + " ").upper()
    print()
    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in vocabularies:
                direction = vocabularies[word]
                break
    if direction in all_exits:
        loc = all_exits[direction]
    else:
        print("You cant go in that direction")
