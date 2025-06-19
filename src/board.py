from typing import List, Tuple
from src.ship import Ship

class Board:
    def __init__(self, size: int = 10):
        self.size = size
        self.grid: List[List[str]] = [['-' for _ in range(size)] for _ in range(size)]
        self.ships: List[Ship] = []
        self.shots_fired = set()

    def place_ship(self, ship: Ship) -> bool:
        for x, y in ship.coordinates:
            if not (0 <= x < self.size and 0 <= y < self.size): 
                return False
            if self.grid[x][y] != '-': 
                return False
        for x, y in ship.coordinates:
            self.grid[x][y] = 'S'
        self.ships.append(ship)
        return True

    def _mark_around(self, x: int, y: int, visited: set):
        if (x, y) in visited or not (0 <= x < self.size and 0 <= y < self.size):
            return
        visited.add((x, y))
        if self.grid[x][y] == '-':
            self.grid[x][y] = 'O'
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx != 0 or dy != 0:
                        self._mark_around(x + dx, y + dy, visited)

    def receive_shot(self, coord: Tuple[int, int]) -> str:
        x, y = coord
        assert isinstance(x, int) and isinstance(y, int), "Współrzędne muszą być intami"
        assert 0 <= x < self.size and 0 <= y < self.size, f"Koordynaty poza planszą: {(x,y)}"
        if coord in self.shots_fired:
            return 'repeat'
        self.shots_fired.add(coord)

        for ship in self.ships:
            if ship.register_shot(coord):
                self.grid[x][y] = 'X'
                if ship.is_sunk():
                    for sx, sy in ship.coordinates:
                        self._mark_around(sx, sy, set())
                    return 'sink'
                return 'hit'

        self.grid[x][y] = 'O'
        return 'miss'

    def all_sunk(self) -> bool:
        return all(ship.is_sunk() for ship in self.ships)

    def display(self) -> None:
        header = '   ' + ' '.join(str(i) for i in range(self.size))
        print(header)
        for idx, row in enumerate(self.grid):
            print(f"{idx:2} " + ' '.join(row))

    def display_masked(self) -> None:
        header = '   ' + ' '.join(str(i) for i in range(self.size))
        print(header)
        for idx, row in enumerate(self.grid):
            visible = ['-' if cell == 'S' else cell for cell in row]
            print(f"{idx:2} " + ' '.join(visible))

    def apply_to_ships(self, func):
        return list(map(func, self.ships))

    def to_dict(self) -> dict:
        return {
            'size': self.size,
            'grid': self.grid,
            'shots_fired': [list(c) for c in self.shots_fired],
            'ships': [s.to_dict() for s in self.ships]
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Board':
        board = cls(data['size'])
        board.grid = data['grid']
        board.shots_fired = set(tuple(c) for c in data.get('shots_fired', []))
        board.ships = [Ship.from_dict(s) for s in data.get('ships', [])]
        return board

class PlayerBoard(Board):
    def display(self):
        print("== TWOJA PLANSZA ==")
        super().display()

class ComputerBoard(Board):
    def display(self):
        print("== PLANSZA KOMPUTERA ==")
        self.display_masked()
