def main():
    current_count = set_total_stone()
    total_players = set_total_players()
    player = 1

    while current_count > 0:
        print(f'\nThere are {current_count} stones left.')
        move = play_each_turn(player)
        current_count -= move
        if current_count < 1:
            break
        player = (player%total_players) + 1

    print(f'Player {player} wins!\n')


def set_total_stone():
    while True:
        try:
            total_count = int(input('\nSet the total number of stones: '))
            return total_count
        except ValueError:
            print("No valid integer! Please try again...")


def set_total_players():
    while True:
        try:
            total_players = int(input('\nHow many players? '))
            return total_players
        except ValueError:
            print("No valid integer! Please try again...")


def play_each_turn(player: int):
    while True:
        input_prompt = f'\n Player {player}, would you like to remove 1 or 2 stones? '
        try:
            move = int(input(input_prompt))
            if move == 1 or move == 2:
                return(move)
            else:
                print('You can only remove 1 or 2 stones.')
        except ValueError:
            print(f'Invalid input. Please type 1 or 2.')


if __name__ == "__main__":
    main()


