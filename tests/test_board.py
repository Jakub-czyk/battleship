from src.board import Board
from src.ship import Ship

def test_place_and_shoot():
    b = Board(5)
    s = Ship("X", 1, [(1,1)])
    assert b.place_ship(s)
    assert b.receive_shot((1,1)) == 'sink'
    assert b.receive_shot((0,0)) == 'miss'
