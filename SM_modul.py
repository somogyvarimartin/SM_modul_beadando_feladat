"""Tanult modul (random modul)

import random

def random_szamok():
    print("Véletlenszerű számok:")
    print(random.randint(1, 100))
    print(random.choice([10, 20, 30, 40]))

random_szamok()"""

"""Bemutatandó modul (datetime)
from datetime import datetime, timedelta

def aktualis_ido():
    most = datetime.now()
    print("Aktuális dátum és idő:", most)

def datum_formazas():
    datum = datetime(2024, 11, 4)
    print("Formázott dátum:", datum.strftime("%Y-%m-%d"))

def jovo_datum_kiszamitasa():
    mai_datum = datetime.today().date()
    jovo_het = mai_datum + timedelta(days=7)
    print("Egy hét múlva:", jovo_het)

aktualis_ido()
datum_formazas()
jovo_datum_kiszamitasa()"""

# sm_modul.py
import tkinter as tk

class SM_dolgozo:
    def __init__(self, nev, kor):
        self.nev = nev
        self.kor = kor

    def bemutatkozas(self):
        return f"Szia, {self.nev} vagyok, {self.kor} éves."

def sm_szamitas(a, b):
    return a + b

def sm_gui():
    def gomb_kattintas():
        print("A gombra kattintottak!")

    root = tk.Tk()
    root.title("SM Program")
    root.geometry("300x200")

    gomb = tk.Button(root, text="Kattints rám!", command=gomb_kattintas)
    gomb.pack(pady=20)

    root.mainloop()

