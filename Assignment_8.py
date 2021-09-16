# 1. Possible directions are evaluated
# 2. Player selects a direction
# 3. Player moves to the new location
# 4. If player is at location 3,1, he wins, else he goes to 1.
# https://github.com/HilmirHMV/TileTraveller.git

# 1. Possible directions are evaluated
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

# 2. Player selects a direction
def direction_selection(location):

    location_strings = location.split(" or ")
    legal_selection = False
    while legal_selection == False: 
        print ("You can travel:", location)
        direction_selection = input('Direction: ')
        upper_direction = direction_selection.upper()
        for direction in location_strings:
            if direction[1] == upper_direction:
                legal_selection = direction[1]
                break

        else:
            print("Not a valid direction!")
    return upper_direction

# 3. Player moves to the new location
def player_move(direction,location):
    if direction == "N":
        location[1] += 1

    elif direction == "S":
        location[1] -= 1

    elif direction == "E":
        location[0] += 1

    elif direction == "W":
        location[0] -= 1

    return location


# Main program
location = [1,1]

# 4. If player is at location 3,1, he wins, else he goes to 1.
while location != [3, 1]:
    location_string = evaluate_direction(location)
    player_selection = direction_selection(location_string)
    location = player_move(player_selection, location)
else:
    print ("Victory!")

