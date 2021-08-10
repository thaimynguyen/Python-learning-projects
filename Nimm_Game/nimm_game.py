"""
Ancient Game of Nimm 

- Two players alternate taking stones until there are zero left.
- The game starts with a pile of 20 stones between the players.
- On a given turn, a player may take either 1 or 2 stone from the center pile.
- The two players continue until the center pile has run out of stones.
- The last player to take a stone loses.


Here's a sample execution:

There are 20 stones left
Player 1 would you like to remove 1 or 2 stones? 2
There are 18 stones left
Player 2 would you like to remove 1 or 2 stones? 2
etc...
There are 2 stones left
Player 1 would you like to remove 1 or 2 stones? 1
There are 1 stones left
Player 2 would you like to remove 1 or 2 stones? 1
Player 1 wins!
"""


def print_stone_count(current_count: int):
    print(f'There are {current_count} stones left. \n')

def print_input_prompt(player: int):
    if player == 1:
        input_prompt = 'Player 1 would you like to remove 1 or 2 stones?\n'
    if player == -1:
        input_prompt = 'Player 2 would you like to remove 1 or 2 stones?\n'
    return input_prompt

def play_each_turn(player: int):
        while True:
            no_of_stones_to_remove = int(input(print_input_prompt(player)))
            if no_of_stones_to_remove in [1, 2]:
                break
            print('Invalid input. Please type 1 or 2.')
        return no_of_stones_to_remove

def print_winner(player: int):
    if player == 1:
        print('Player 1 wins!\n')
    if player == -1:
        print('Player 2 wins!\n')
    
def main():
    current_stone_count = 20
    winner = None
    player = 1

    while not winner:
        print_stone_count(current_stone_count)
        current_stone_count -= play_each_turn(player)
        player *= -1

        if current_stone_count < 1:
            winner = player
            break
    
    print_winner(winner)

if __name__ == "__main__":
    main()








