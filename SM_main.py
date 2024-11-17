# main.py
from SM_modul import SM_dolgozo, sm_szamitas, sm_gui

# SM_Dolgozo osztály használata
dolgozo = SM_dolgozo("Somogyvári Martin", 25)
print(dolgozo.bemutatkozas())

# sm_szamitas függvény használata
eredmeny = sm_szamitas(10, 15)
print(f"A számítás eredménye: {eredmeny}")

# sm_gui függvény használata (grafikus felület megnyitása)
sm_gui()
