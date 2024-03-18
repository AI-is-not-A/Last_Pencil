num_pencils_table = 0
players = ["John", "Jack"]
on_turn = ""


def set_start_pencils():
    global num_pencils_table
    while num_pencils_table == 0:
        pencils = input("How many pencils would you like to use:")
        try:
            num_pencils_table = int(pencils)
        except ValueError:
            print("The number of pencils should be numeric.")
            continue

        if num_pencils_table == 0:
            print("The number of pencils should be positive")
        elif num_pencils_table < 0:
            print("he number of pencils should be numeric (the minus sign is not a numeric)")
            num_pencils_table = 0
        else:
            num_pencils_table = int(pencils)


def set_first_player():
    global on_turn
    on_turn = input(f"Who will be the first ({players[0]}, {players[1]}):")
    while on_turn != players[0] and on_turn != players[1]:
        on_turn = input(f"Choose between {players[0]} and {players[1]}:")


def next_player():
    global on_turn
    if on_turn == players[0]:
        on_turn = players[1]
    else:
        on_turn = players[0]


def get_pencils_taken():
    while True:
        try:
            pencils_taken_by_player = int(input())
        except ValueError:
            print("Possible values: '1', '2' or '3'")
            continue
        if pencils_taken_by_player != 1 and pencils_taken_by_player != 2 and pencils_taken_by_player != 3:
            print("Possible values: '1', '2' or '3'")
            continue
        if pencils_taken_by_player > num_pencils_table:
            print("Too many pencils were taken")
            continue
        return pencils_taken_by_player


def is_winning_postion():
    global num_pencils_table
    if num_pencils_table == 1 or (num_pencils_table - 5) % 4 == 0:
        return False
    return True


def get_pencils_num():
    global num_pencils_table
    if num_pencils_table % 4 == 0:
        return 3
    if (num_pencils_table - 3) % 4 == 0:
        return 2
    return 1


set_start_pencils()
set_first_player()

while num_pencils_table != 0:
    print(num_pencils_table * "|")
    print(f"{on_turn}'s turn:")
    if on_turn == players[0]:
        num_pencils_table -= get_pencils_taken()
    elif is_winning_postion():
        pencils_taken = get_pencils_num()
        num_pencils_table -= pencils_taken
        print(pencils_taken)
    else:
        num_pencils_table -= 1
        print(1)
    next_player()

print(f"{on_turn} won!")
