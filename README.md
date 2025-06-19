# Battleship (Gra w statki)

Tekstowa gra w statki: gracz vs komputer.  
3 statki tego samego rozmiaru (2, 3, 4 pola) losowo rozmieszczone.  
Dwie plansze obok siebie:  
- Twoja (ze statkami i strzałami komputera)  
- Komputera (tylko strzały gracza)

## Uruchomienie

```bash
python -m venv venv
# Windows PowerShell
.\venv\Scripts\Activate.ps1
# lub cmd.exe
.\venv\Scripts\activate.bat

pip install -r requirements.txt
pytest
python -m src.ui
