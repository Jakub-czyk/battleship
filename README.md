# Battleship (Gra w statki)

Tekstowa gra w statki: gracz vs komputer.

Rozgrywka odbywa się na dwóch planszach:
- Twoja plansza: zawiera Twoje statki i trafienia komputera.
- Plansza przeciwnika (komputera): pokazuje tylko trafienia dokonane przez Ciebie.

Każdy gracz ma 3 statki o długościach 2, 3 i 4 pola, rozmieszczone losowo.

---

## Uruchomienie gry

### Krok 1: Stwórz i aktywuj środowisko wirtualne

```bash
python -m venv venv

# Windows PowerShell
.env\Scripts\Activate.ps1

# Windows CMD
.env\Scriptsctivate.bat

# Linux / macOS
source venv/bin/activate
```

### Krok 2: Zainstaluj wymagania

```bash
pip install -r requirements.txt
```

### Krok 3: Uruchom grę

```bash
python -m src.ui
```

---

## Testowanie

Projekt zawiera testy jednostkowe i funkcjonalne:

```bash
pytest
```

Aby sprawdzić jakość kodu:

```bash
flake8 src tests
```

---


## Wygenerowany wykres

Po zakończeniu rozgrywki generowany jest wykres liczby trafień na turę:

Plik wyjściowy: `reports/hits.png`

---

## Diagram klas

```mermaid
classDiagram
    class Ship {
        +int length
        +bool horizontal
        +List[Tuple[int, int]] coordinates
        +is_sunk()
    }

    class Board {
        +int size
        +List[List[Cell]]
        +place_ship(ship, row, col, horizontal)
        +receive_shot(row, col)
    }

    class PlayerBoard {
        +ships: List[Ship]
        +receive_shot()
    }

    class ComputerBoard {
        +ships: List[Ship]
        +auto_shoot()
    }

    PlayerBoard --> Ship
    ComputerBoard --> Ship
    Board --> Ship
```

---

