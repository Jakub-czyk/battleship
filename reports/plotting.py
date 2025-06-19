import matplotlib.pyplot as plt
from typing import List

def plot_hits_over_turns(hits_per_turn: List[int], filename: str = "reports/hits.png"):
    assert hits_per_turn, "Brak danych do wykresu"
    
    turns = list(range(1, len(hits_per_turn) + 1))
    
    plt.figure()
    plt.plot(turns, hits_per_turn, marker='o', linestyle='-', color='blue')
    plt.xlabel("Tura")
    plt.ylabel("Liczba trafień")
    plt.title("Trafienia na turę")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    print(f"Wykres zapisano do pliku: {filename}")
