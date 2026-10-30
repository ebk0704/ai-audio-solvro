
import librosa
import librosa.display
import numpy as np
import matplotlib
import soundfile as sf
from pathlib import Path

matplotlib.use("QtAgg")
import matplotlib.pyplot as plt

plik = librosa.ex("libri2")

dzwiek, sr = librosa.load(plik, sr=None, duration=10)

widmo = librosa.stft(dzwiek)


# Tworze tablice czestotliwosci
czestotliwosci = librosa.fft_frequencies(
    sr=sr, n_fft=2048
)

# Wybieram czestotliwosci z przedzialu w Hz
maska = (czestotliwosci < 500) | (czestotliwosci > 4000)
# Tworze kopie widma
widmo_filtrowane = widmo.copy()

# Zeruje wybrane wspolczynniki
widmo_filtrowane[maska, :] = 0


# Odtwarzam probki z przefiltrowanego widma
dzwiek_filtrowany = librosa.istft(
    widmo_filtrowane,
    length=len(dzwiek)
)



energia_oryginal = np.sum(dzwiek ** 2)

energia_filtrowany = np.sum(dzwiek_filtrowany ** 2)

procent_energii = (energia_filtrowany / energia_oryginal) * 100

print("Pozostala energia:", round(procent_energii, 2), "%")



amplitudy = np.abs(widmo)

amplitudy_db = librosa.amplitude_to_db(
    amplitudy, ref=np.max
)

obraz = librosa.display.specshow(
    amplitudy_db,
    sr=sr,
    x_axis="time",
    y_axis="hz"
)

plt.colorbar(obraz, format="%+d dB")

plt.title("Spektrogram ludzkiego glosu")
plt.xlabel("Czas (sekundy)")
plt.ylabel("Czestotliwosc (Hz)")



# Obliczam amplitudy przefiltrowanego widma
amplitudy_filtrowane = np.abs(widmo_filtrowane)

# Zamieniam je na decybele
amplitudy_filtrowane_db = librosa.amplitude_to_db(
    amplitudy_filtrowane,
    ref=np.max(amplitudy)
)

# Tworze nowe okno wykresu
plt.figure()

# Rysuje spektrogram przefiltrowanego nagrania
obraz_filtrowany = librosa.display.specshow(
    amplitudy_filtrowane_db,
    sr=sr,
    x_axis="time",
    y_axis="hz"
)

plt.colorbar(obraz_filtrowany, format="%+d dB")
plt.title("Spektrogram po filtracji")
plt.xlabel("Czas (sekundy)")
plt.ylabel("Czestotliwosc (Hz)")



# Wskazuje folder outputs w naszym projekcie
folder = Path(__file__).resolve().parent / "outputs"

# Tworze folder, jesli jeszcze nie istnieje
folder.mkdir(exist_ok=True)

# Zapisuje oryginalne nagranie
sf.write(folder / "oryginal2.wav", dzwiek, sr)

# Zapisuje nagranie po filtracji
sf.write(folder / "pasmo2_500_4000.wav", dzwiek_filtrowany, sr)

print("Nagrania zostaly zapisane!")



print("Liczba czestotliwosci:", len(czestotliwosci))
print("Pierwsze 5 czestotliwosci:", czestotliwosci[:5])
print("Liczba wyzerowanych wierszy:", np.sum(maska))


plt.show()
