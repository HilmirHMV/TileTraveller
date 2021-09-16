# -1. Evaluate player location
# 0. Possible directions are evaluated
# 1. Player gets info about valid directions
# 2. Player selects a direction
# 3. direction is evaluated, if false go to 2.
# 4. Player moves to the new location
# 5. If player is at location 3,1, he wins, else he goes to 1.

# .-1
def evaluate_direction(location):
    victory_condition = False
    if location == [1, 1] or location == [2,1] or location[3,1]:
        possible_directions = "(N)orth"
        

    elif location == [1, 2]:
        possible_directions = "(N)orth", "(E)ast", "(S)outh"
        

    elif location == [1, 3]:
        possible_directions = "(E)ast", "(S)outh"
        

    elif location == [2, 2] or location == [3, 3]:
        possible_directions = "(S)outh", "(W)est"
        

    elif location == [2, 3]:
        possible_directions = "(E)ast", "(W)est"
        

    elif location == [3, 2]:
        possible_directions = "(N)orth", "(S)outh"
        
    
    elif location == [3, 1]:
        victory_condition = True

    return [possible_directions, victory_condition]


# 4.
def move(direction,location):
    if direction.lower == "n":
        if location[1] == 3:
            print("Not a valid direction!")
        else:
            location[1] += 1

    elif direction.lower == "s":
        if location[1] == 1:
            print("Not a valid direction!")
        else:
            location[1] -= 1

    elif direction.lower == "e":
        if location[0] == 3:
            print("Not a valid direction!")
        else:
            location[0] += 1

    elif direction.lower == "w":
        if location[0] == 1:
            print("Not a valid direction!")
        else:
            location[0] -= 1

    else:
        print("Not a valid direction!")

    return location


