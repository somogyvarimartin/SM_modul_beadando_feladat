SM Program

Hallgató:
Somogyvári Martin

Feladat Leírása
Ez a program a Python programozás alapjait ismerteti három modul, eseménykezelés és grafikus felhasználói felület révén. A programnak meg kell felelnie a következő követelményeknek:
Egy tanult modul (random), amely a véletlenszám-generálás funkcióját biztosítja,
Egy bemutatandó modul (datetime), amely a dátumok és idő kezelésére szolgál,
Egy saját modul (sm_modul.py), amely saját függvényt és osztályt tartalmaz, valamint egy egyszerű grafikus felhasználói felületet eseménykezeléssel.

Modulok és az abban használt Függvények
Tanult Modul: random
random.randint(a, b): Véletlenszerű számot generál az a és b közötti tartományban.
random.choice(lista): Kiválaszt egy véletlenszerű elemet a megadott lista elemei közül.

Bemutatandó Modul: datetime
datetime.now(): Visszaadja az aktuális dátumot és időt.
datetime.strftime(formátum): A dátumot egy meghatározott formátumban jeleníti meg.
timedelta(days=n): Megnöveli a dátumot egy specifikus időtartammal.

Saját modul: sm_modul.py
Osztály: SM_Dolgozo
__init__(self, nev, kor): Az osztály attribútumainak (nev és kor) inicializálása.
bemutatkozas(self): Visszaad egy üdvözlő szöveget.

Függvények:
sm_szamitas(a, b): Visszaadja a és b összegét.
sm_gui(): Aktiválja a grafikus felületet, ami tartalmaz egy eseménykezeléssel ellátott gombot. A gomb megnyomásakor üzenet jelenik meg a konzolon.

Program felépítése
Indítás: main.py
Alapablak: root
Programnév: app
