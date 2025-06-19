import pytest
from src.board import Board
from src.ship import Ship

def test_full_game_play():
    # 1. Setup
    b = Board(size=4)
    # Ustawiamy 2 małe statki
    s1 = Ship("A", 1, [(0,0)])
    s2 = Ship("B", 2, [(1,1),(1,2)])
    assert b.place_ship(s1)
    assert b.place_ship(s2)

    # 2. Kolejne strzały: najpierw pudło, potem trafienia
    assert b.receive_shot((3,3)) == 'miss'
    assert not b.all_sunk()

    # Trafiamy w s1 => zatopiony
    assert b.receive_shot((0,0)) == 'sink'
    assert not b.all_sunk()

    # Trafiamy w części B
    assert b.receive_shot((1,1)) == 'hit'
    assert not b.all_sunk()

    # Drugie pole B => zatopiony
    assert b.receive_shot((1,2)) == 'sink'
    # Teraz wszystkie zatopione
    assert b.all_sunk()

    # Kolejny strzał w już używane pole
    assert b.receive_shot((1,2)) == 'repeat'
