# NAGY Béla 2023.04.12
import random
import tkinter as tk
from tkinter import ttk

#honap2829 = ['Február']
honap30 = ['Április', 'Június', 'Szeptember', 'November']
honap31 = ['Január', 'Március', 'Május', 'Július', 'Augusztus', 'Október', 'December']
Februar = 'Február'
napok_szama = 1 # Nullával nem lehet osztani

# ellenőrizzük, hogy szükőév-e
def szokoev(ev):
    return ev % 4 == 0 and (ev % 100 != 0 or ev % 400 == 0)



def generalas():
    global honap_neve, nap_ma, min_lista, max_lista, napok_szama
    nap_ma = []
    min_lista = []
    max_lista = [] #üres listák létrehozása
    ev = random.randint(1900,2050)
    napok_szama = random.randint(28, 31)  # létező hónap napjainak generálása
    if napok_szama == 31:
        honap_neve = random.choice(honap31)
    elif napok_szama == 30:
        honap_neve = random.choice(honap30)
    elif napok_szama == 28 or napok_szama == 29:
        honap_neve = Februar
        napok_szama = 29 if szokoev(ev) else 28  # Február napjainak számát a szökőév alapján állítjuk be
    ...
    # hőmérsékletek generálása
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

    return (nap_ma, min_lista, max_lista, napok_szama,ev)


def szamitas(napok_szama):
    kulonbseg = [max_lista[i] - min_lista[i] for i in range(napok_szama)]
    return kulonbseg


# átlagok kiszámítása
def atlagok():
    global atlag_max, atlag_min, legalacsonyabb, legmagasabb  # , legkis_label, legnagy_label  <-- felesleges
    atlag_max = sum(max_lista) / napok_szama  # a lista öszege osztva a napok számával
    atlag_min = sum(min_lista) / napok_szama  # a lista öszege osztva a napok számával
    legalacsonyabb = min(min_lista)
    legmagasabb = max(max_lista)
    return atlag_min, atlag_max, legalacsonyabb, legmagasabb

def uj_adatok():

    global ev
    nap_ma, min_lista, max_lista, napok_szama, ev = generalas()

    atlag_max,atlag_min,legalacsonyabb,legmagasabb = atlagok()

    kulonbseg = szamitas(napok_szama)
    tablazat.delete(*tablazat.get_children())

    honap_neve_str = "".join(honap_neve)
    cimke2.config(text=f"Az adott hónap: {ev}  {honap_neve_str:12}")

    napok_szama_str = str(napok_szama)
    cimke3.config(text="A napok száma: " + napok_szama_str)

    atlag_min_label.config(text="Az átlagos minimum hőmérséklet: {:.2f} °C".format(atlag_min))
    atlag_max_label.config(text="Az átlagos maximum hőmérséklet: {:.2f} °C".format(atlag_max))

    legalacsonyabb = min(min_lista)
    legmagasabb = max(max_lista)

    legkis_label.config(text="A legalacsonyabb hőmérséklet: {:.2f} °C".format(legalacsonyabb))
    legnagy_label.config(text="A legmagasabb hőmérséklet: {:.2f} °C".format(legmagasabb))

    for i in range(napok_szama):
        tablazat.insert(parent="", index=i, values=(
        honap_neve, nap_ma[i], f"{min_lista[i]:.2f} °C", f"{max_lista[i]:.2f} °C", f"{kulonbseg[i]:.2f} °C"))

def kilépés():
    root.destroy()

# ======================   GUI ===========================================

# GUI létrehozása
root = tk.Tk()
root.geometry("1200x600")  # a felület, ablak mérete
root.title("Hőingadozás")  # az ablak neve

# Címke hozzáadása
cimke1 = tk.Label(root, text="Generált Hőingadozás napi bontásban")
cimke1.grid()

# Adatok generálása
nap_ma, min_lista, max_lista, napok_szama,ev = generalas()
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

# Frame létrehozása a táblázat alatt
masodik_frame = tk.Frame(root)
masodik_frame.grid(row=3, column=0, padx=10, pady=5)

# Button elhelyezése a Frame-en belül
uj_adatok_gomb = tk.Button(alatta_frame, text="Új adatok generalasa", command=uj_adatok)
uj_adatok_gomb.pack(side=tk.RIGHT, padx=5, pady=5)

# Címkék elhelyezése a Frame-en belül
cimke2 = tk.Label(alatta_frame, text=(f"Az adott hónap: {ev}  {honap_neve_str}"))
cimke2.pack(side=tk.LEFT, padx=5, pady=5)

cimke3 = tk.Label(alatta_frame, text="A napok száma " + str(napok_szama))
cimke3.pack(side=tk.LEFT, padx=10, pady=5)

# Átlagok kiírása
atlagok()
atlag_min_label = tk.Label(alatta_frame, text="Az átlagos minimum hőmérséklet: {:.2f} °C".format(atlag_min))
atlag_max_label = tk.Label(alatta_frame, text="Az átlagos maximum hőmérséklet: {:.2f} °C".format(atlag_max))
atlag_min_label.pack(side=tk.LEFT, padx=10, pady=5)
atlag_max_label.pack(side=tk.LEFT, padx=10, pady=5)
# legek kiírása
legkis_label = tk.Label(masodik_frame, text="A legalacsonyabb hőmérséklet: {:.2f} °C".format(legalacsonyabb))
legnagy_label = tk.Label(masodik_frame, text="A legmagasabb hőmérséklet: {:.2f} °C".format(legmagasabb))
legkis_label.grid(row=0, column=0, padx=10, pady=5)
legnagy_label.grid(row=0, column=1, padx=10, pady=5)
kilepes_gomb = tk.Button(masodik_frame, text="Kilépés", command=kilépés)
kilepes_gomb.grid(row=0, column=5, padx=10, pady=5)

root.mainloop()