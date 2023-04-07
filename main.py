import random
import tkinter as tk
from tkinter import ttk

nap_ma = []
min_lista = []
max_lista = []
honap2829 = ['Február']
honap30 = ['Április', 'Június', 'Szeptember', 'November']
honap31 = ['Január', 'Március', 'Május', 'Július', 'Augusztus', 'Október', 'December']
napok_szama = 1
atlag_max = 0


def generalas():
    global honap_neve, nap_ma, min_lista, max_lista, napok_szama
    nap_ma = []
    min_lista = []
    max_lista = []
    napok_szama = random.randint(28, 31)  # létező hónap napjainak generálása
    if napok_szama == 31:
        honap_neve = random.choice(honap31)
    elif napok_szama == 30:
        honap_neve = random.choice(honap30)
    elif napok_szama == 28 or 29:
        honap_neve = honap2829

    for i in range(napok_szama):
        nap_ma1 = (f'{i + 1}. nap ')
        nap_ma.append(nap_ma1)
        minimum_homerseklet = round(random.uniform(-10, 30), 2)  # kerekítve 2 tizedes jegyre
        maximum_homerseklet = round(random.uniform(-10, 30), 2)  # kerekítve 2 tizedes jegyre

        # Addig generáljuk a maximum_homerseklet értékét, amíg az nem nagyobb a minimum_homerseklet értékénél
        while maximum_homerseklet <= minimum_homerseklet:
            maximum_homerseklet = round(random.uniform(-10, 30), 2)

        min_lista.append(minimum_homerseklet)
        max_lista.append(maximum_homerseklet)

    return (nap_ma, min_lista, max_lista, napok_szama)


def szamitas(napok_szama):
    global nap_ma  # hozzáadott sor
    kulonbseg = [max_lista[i] - min_lista[i] for i in range(napok_szama)]
    return kulonbseg


# átlagok kiszámítása
def atlagok():
    global atlag_max, atlag_min
    atlag_max = sum(max_lista) / napok_szama
    atlag_min = sum(min_lista) / napok_szama
    return f'Az átlagos minimum hőmérséklet: {atlag_min:.2f} °C\nAz átlagos maximum hőmérséklet: {atlag_max:.2f} °C'


atlagok()


def uj_adatok():
    global napok_szama, honap_neve, nap_ma, min_lista, max_lista, atlag_min_label, atlag_max_label
    generalas()
    atlagok()
    kulonbseg = szamitas(napok_szama)
    tablazat.delete(*tablazat.get_children())

    honap_neve_str = "".join(honap_neve)
    cimke2.config(text="A hónap neve: " + honap_neve_str)

    napok_szama_str = str(napok_szama)
    cimke3.config(text="A napok száma: " + napok_szama_str)

    atlag_min_label.config(text="Az átlagos minimum hőmérséklet: {:.2f} °C".format(atlag_min))
    atlag_max_label.config(text="Az átlagos maximum hőmérséklet: {:.2f} °C".format(atlag_max))

    atlag_min_label.pack(side=tk.LEFT, padx=10, pady=5)
    atlag_max_label.pack(side=tk.LEFT, padx=10, pady=5)

    for i in range(napok_szama):
        if i < napok_szama:
            tablazat.insert(parent="", index=i, values=(
            honap_neve, nap_ma[i], f"{min_lista[i]:.2f} °C", f"{max_lista[i]:.2f} °C", f"{kulonbseg[i]:.2f} °C"))
        else:
            tablazat.insert(parent="", index=i, values=("", "", "", "", ""))


# _____________________________ GUI ______________________________________________________


# GUI létrehozása
root = tk.Tk()
root.geometry("1200x500")  # a felület, ablak mérete
root.title("Hőingadozás")  # az ablak neve

# Címke hozzáadása
cimke1 = tk.Label(root, text="Generált Hőingadozás napi bontásban")
cimke1.grid()

# Adatok generálása
nap_ma, min_lista, max_lista, napok_szama = generalas()
kulonbseg = szamitas(napok_szama)

# Táblázat előállítása
headers = ["Hónap", "Nap", "Minimum hőmérséklet", "Maximum hőmérséklet", "Hőmérséklet-különbség"]
tablazat = ttk.Treeview(root, columns=headers, show="headings", height=20)  # height a megjelenítendő sorik száma

# Oszlopok címkéinek hozzáadása
for col in headers:
    tablazat.heading(col, text=col)

# Adatok hozzáadása a táblázathoz
for i in range(napok_szama):
    tablazat.insert(parent="", index=i, values=(
    honap_neve, nap_ma[i], f"{min_lista[i]:.2f} °C", f"{max_lista[i]:.2f} °C", f"{kulonbseg[i]:.2f} °C"))

# tablázat megjelenítése
tablazat.grid()
honap_neve_str = "".join(honap_neve)
napok_szama_str = str(napok_szama)

# Frame létrehozása a táblázat alatt
alatta_frame = tk.Frame(root)
alatta_frame.grid(row=2, column=0, padx=10, pady=10)

# Button elhelyezése a Frame-en belül
uj_adatok_gomb = tk.Button(alatta_frame, text="Új adatok generalasa", command=uj_adatok)
uj_adatok_gomb.pack(side=tk.RIGHT, padx=5, pady=5)

# Label-ek elhelyezése a Frame-en belül
cimke2 = tk.Label(alatta_frame, text="A hónap neve: " + honap_neve_str)
cimke2.pack(side=tk.LEFT, padx=5, pady=5)

cimke3 = tk.Label(alatta_frame, text="A napok száma " + str(napok_szama))
cimke3.pack(side=tk.LEFT, padx=10, pady=5)

# Átlagok kiírása
atlagok()
atlag_min_label = tk.Label(alatta_frame, text="Az átlagos minimum hőmérséklet: {:.2f} °C".format(atlag_min))
atlag_max_label = tk.Label(alatta_frame, text="Az átlagos maximum hőmérséklet: {:.2f} °C".format(atlag_max))
atlag_min_label.pack(side=tk.LEFT, padx=10, pady=5)
atlag_max_label.pack(side=tk.LEFT, padx=10, pady=5)

root.mainloop()