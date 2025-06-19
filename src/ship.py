from typing import List, Tuple

class Ship:
    def __init__(self, name: str, length: int, coordinates: List[Tuple[int, int]]):
        self.name = name
        self.length = length
        self.coordinates = coordinates  
        self.hits = set()              

    def register_shot(self, coord: Tuple[int, int]) -> bool:
        """Zwraca True jeśli statek trafiony."""
        if coord in self.coordinates:
            self.hits.add(coord)
            return True
        return False

    def is_sunk(self) -> bool:
        """Zwraca True jeśli liczba trafień == długość."""
        return len(self.hits) >= self.length
    
    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'length': self.length,
            'coordinates': self.coordinates,
            'hits': list(self.hits)
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Ship':
        ship = cls(data['name'], data['length'], [tuple(c) for c in data['coordinates']])
        ship.hits = set(tuple(c) for c in data.get('hits', []))
        return ship
