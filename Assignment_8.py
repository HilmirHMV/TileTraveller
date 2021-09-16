# 1. Possible directions are evaluated
# 2. Player selects a direction
# 3. direction is evaluated, if false go to 2.
# 4. Player moves to the new location
# 5. If player is at location 3,1, he wins, else he goes to 1.

# .1
def evaluate_direction(location):
    if location == [1, 1] or location == [2,1]:
        possible_directions = "(N)orth."
        
    elif location == [1, 2]:
        possible_directions = "(N)orth or (E)ast or (S)outh."
        
    elif location == [1, 3]:
        possible_directions = "(E)ast or (S)outh."
        
    elif location == [2, 2] or location == [3, 3]:
        possible_directions = "(S)outh or (W)est."
        
    elif location == [2, 3]:
        possible_directions = "(E)ast or (W)est."
        
    elif location == [3, 2]:
        possible_directions = "(N)orth or (S)outh."

    return possible_directions

# 2.
def direction_selection(location):

    location_string = location.split(" or ")
    while True: #finna eitthvað annað en True
        direction_selection = input('Direction:')
        upper_direction = direction_selection.upper()
        for direction in location_string:
            if direction[1] == upper_direction:
                return upper_direction
        print("Not a valid direction!", direction[1], direction_selection)
                    

# 3.
 
    
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

location = [1,1]
location_string = evaluate_direction(location)
print(location_string)
direction_selection(location_string)
