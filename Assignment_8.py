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
