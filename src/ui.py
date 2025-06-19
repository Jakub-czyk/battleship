import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import random
from time import sleep
from functools import reduce

from src.board import PlayerBoard, ComputerBoard
from src.ship import Ship
from src.decorators import log_action
from src.utils.serializers import save_to_file, load_from_file

SAVE_PATH = 'data/savegame.json'
SHIP_SIZES = [2, 3, 4]

def coord_from_input(s: str):
    x, y = map(int, s.strip().split(','))
    return x, y

def random_place_ships(board, sizes=SHIP_SIZES):
    for size in sizes:
        placed = False
        while not placed:
            orientation = random.choice(['h', 'v'])
            if orientation == 'h':
                x = random.randrange(0, board.size)
                y = random.randrange(0, board.size - size + 1)
                coords = [(x, y + i) for i in range(size)]
            else:
                x = random.randrange(0, board.size - size + 1)
                y = random.randrange(0, board.size)
                coords = [(x + i, y) for i in range(size)]
            placed = board.place_ship(Ship(f"Ship{size}", size, coords))

@log_action
def setup_board(randomize=True):
    board = PlayerBoard(8) if randomize else PlayerBoard(8)
    if randomize:
        random_place_ships(board)
    return board

def print_boards(player, computer):
    print(" TWOJA PLANSZA:".ljust(24) + "PLANSZA KOMPUTERA:")
    header = '   ' + ' '.join(str(i) for i in range(player.size))
    print(header.ljust(24) + header)
    for i in range(player.size):
        row_p = ' '.join(player.grid[i])
        row_c = ' '.join(['-' if c == 'S' else c for c in computer.grid[i]])
        print(f"{i:2} {row_p}".ljust(24) + f"{i:2} {row_c}")

def main():
    player_board = PlayerBoard(8)
    computer_board = ComputerBoard(8)
    random_place_ships(player_board)
    random_place_ships(computer_board)

    available_moves = [(x, y) for x in range(player_board.size) for y in range(player_board.size)]
    random.shuffle(available_moves)

    print("=== Gra w statki: Ty vs Komputer ===")
    while True:
        print_boards(player_board, computer_board)

        inp = input("Twój strzał (x,y): ")
        try:
            coord = coord_from_input(inp)
        except:
            print("Błędny format, użyj: x,y")
            continue

        result = computer_board.receive_shot(coord)
        if result == 'repeat':
            print("Już tu strzelałeś, spróbuj ponownie.")
            continue
        print(f"Twój strzał: {result.upper()}")
        sunk_list = player_board.apply_to_ships(lambda s: s.is_sunk())
        print(f"Zatopione Twoje jednostki: {sum(sunk_list)}/{len(sunk_list)}")
        if computer_board.all_sunk():
            print("Wygrałeś! Wszystkie statki komputera zatopione.")
            break

        sleep(0.5)
        comp_coord = available_moves.pop()
        comp_result = player_board.receive_shot(comp_coord)
        print(f"Komputer strzela w {comp_coord}: {comp_result.upper()}")
        remaining = list(filter(lambda s: not s.is_sunk(), computer_board.ships))
        print(f"Pozostało statków przeciwnika: {len(remaining)}")
        total_hits = reduce(lambda acc, ship: acc + len(ship.hits), player_board.ships, 0)
        print(f"Łącznie Twoich trafień: {total_hits}")

        if player_board.all_sunk():
            print("Przegrałeś, komputer zatopił wszystkie Twoje statki.")
            break


if __name__ == '__main__':
    main()
