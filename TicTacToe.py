from random import randint

# interface class
class Interface():
    def __init__(self):
        self.menu = [
            ["+----------------------------+"],
            ["|          TICTACTOE         |"],
            ["+----------------------------+"],
            ["| 1. PvP                     |"],
            ["| 2. PvE                     |"],
            ["| 3. Exit                    |"],
            ["+----------------------------+"],
        ]
        self.round = [
            ["+----------------------------+"],
            ["|     TICTACTOE | ROUNDS     |"],
            ["+----------------------------+"],
            ["| 1. One Shot                |"],
            ["| 2. 3 Rounds                |"],
            ["| 3. Exit                    |"],
            ["+----------------------------+"],
        ]
        self.x_value = 0
        self.o_value = 0
        pass

    # displays
    def display_menu(self):
        print("\n".join("".join(map(str, row)) for row in self.menu))

    def display_round(self):
        print("\n".join("".join(map(str, row)) for row in self.round))

    def display_game_head(self):
        game_head = [
            ["+-----------------------------+"],
            ["|          TICTACTOE          |"],
            ["+-----------------------------+"],
            [f"|         x: {self.x_value} | o: {self.o_value}         |"],
            ["+-----------------------------+"],
        ]

        print("\n".join("".join(map(str, row)) for row in game_head))

    def display_cross_game(self, cross_dict):
        print("\n".join("|            " + " ".join(map(str, row)) + "            |" for row in cross_dict))
        print("+-----------------------------+")

    # setters
    def set_x_value(self, n):
        self.x_value = n

    def set_o_value(self, n):
        self.o_value = n

# display the game
def display_game(cross_dict):
    print("\n".join(" ".join(map(str, row)) for row in cross_dict))

# verify if the place is avaliable
def verify_place(cross_dict, place):
    return any(str(place) == x for y in cross_dict for x in y)

# change the place into a "x" or "o"
def change_game(cross_dict, place, player):
    return [
        [f"{str(player)}" if value == place else value for value in row]
        for row in cross_dict
    ]

# verify if someone wins
def verify_win(cross_dict, player):
    # verify the diagonal
    if all(cross_dict[i][i] == player for i in range(3)) or all(cross_dict[i][2-i] == player for i in range(3)):
        return True

    # verify a entire row
    for row in cross_dict:
        if all(value == player for value in row):
            return True

    # verify the entire column
    if all(cross_dict[i][0] == player for i in range(3)):
        return True

    return False

# verify if any place are avaliable to play, if not declare drawn
def is_board_avaliable(cross_dict):
    return any(str(value).isdigit() for row in cross_dict for value in row)

# to make the code more cleaner, this function resets the game
def reset_game():
    return [
            ["0", "1", "2"],
            ["3", "4", "5"],
            ["6", "7", "8"]
        ]

# just space
def space():
    [print() for i in range(10)]


interface = Interface()
while True:
    while True:
        space()
        interface.display_menu()
        print()

        # Get the player's choice. If the input is not a number, return an invalid option.
        try:
            option = int(input(" +- Choose your opponent: "))

            if option > 3 or option < 1:
                print()
                print(" - Please select an valid option...")
                print()
                input("...")
            else:
                break
        except ValueError:
            print()
            print(" - Please select an valid option...")
            print()
            input("...")

        # if it be more then 3, it gonna return an invalid option.
        

    # if the player option be 3, it gonna break the while. But 
    if option == 3:
        break

    mode = "pvp" if option == 1 else "pve"

    # display the mode
    while True:
        space()
        interface.display_round()
        print()

        # Get the player's choice. If the input is not a number, return an invalid option.
        try:
            option = int(input(" +- Choose how many rounds: "))

            if option > 3 or option < 1:
                print()
                print(" - Please select an valid option...")
                print()
                input("...")
            else:
                break
        except ValueError:
            print()
            print(" - Please select an valid option...")
            print()
            input("...")

        

    # if the player option be 3, it gonna break the while. But 
    if option == 3:
        break

    one_shot = True if option == 1 else False
    rounds = 3 if not one_shot else 0 

    cross = reset_game()

    game = True
    # if the turn is True it means that "x" should play, if false "o" should play
    turn = True
    x_score = 0
    o_score = 0
    interface.set_x_value(x_score)
    interface.set_o_value(o_score)
    while (game):
        space()
        print()
        interface.display_game_head()
        interface.display_cross_game(cross)
        print()

        # if pve was selected, the pc gonna play in a random place, in the future we gonna change it to anything more inteligent
        if mode == "pve" and not turn:
            place = randint(0, 8)
            while not verify_place(cross, place):
                place = randint(0, 8)

            place = str(place)
        else:
            place = str(input(f" +- {"x" if turn else "o"} Turn: "))

        if verify_place(cross, place):
            space()
            cross = change_game(cross, place, "x" if turn else "o")

            if verify_win(cross, "x" if turn else "o"):
                if turn:
                    x_score += 1
                    interface.set_x_value(x_score)
                else:
                    o_score += 1
                    interface.set_o_value(o_score)

                interface.display_game_head()
                interface.display_cross_game(cross)
                print()
                print(f" +- {"x" if turn else "o"} Win!!!")
                print()
                input("...")

                cross = reset_game()
                if rounds == 0 or x_score == 2 or o_score == 2:
                    game = not game
                    break
                else:
                    rounds -= 1

            display_game(cross)

            turn = not turn
        else:
            print()
            print(" - This already has been taken or dont exist, please select another place...")
            print()
            input("...")

        if not is_board_avaliable(cross):
            space()
            interface.display_game_head()
            interface.display_cross_game(cross)
            print()
            print(" +- Drawn!")
            print()
            input("...")
            print()
            cross = reset_game()

# that program its an study project made by @Deyvii, if you payed for this sorry but its a scam