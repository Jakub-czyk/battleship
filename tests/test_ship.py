import pytest
from src.ship import Ship

def test_hit_and_sink():
    ship = Ship("T", 1, [(0,0)])
    assert ship.register_shot((0,0)) is True
    assert ship.is_sunk()
