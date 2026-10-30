
import matplotlib
matplotlib.use("QtAgg")

import matplotlib.pyplot as plt
from pathlib import Path

# Granice czestotliwosci, ktore testowalismy
granice = [3000, 4000, 5000, 7000]

# Wyniki eksperymentow
energia_libri1 = [99.33, 99.79, 99.94, 99.99]
energia_libri2 = [98.85, 99.88, 99.94, 99.99]

# Tworze wykres
plt.figure(figsize=(9, 5))

plt.plot(granice, energia_libri1, marker="o", label="libri1")
plt.plot(granice, energia_libri2, marker="o", label="libri2")

plt.title("Wplyw usuwania wysokich czestotliwosci na energie")
plt.xlabel("Gorna granica pasma (Hz)")
plt.ylabel("Pozostala energia (%)")

plt.xticks(granice)
plt.ylim(98, 100.1)
plt.legend()
plt.grid(True)

# Zapisuje wykres do pliku
folder = Path(__file__).resolve().parent / "outputs"
folder.mkdir(exist_ok=True)

plt.savefig(folder / "porownanie_energii.png", dpi=150)

plt.show()
