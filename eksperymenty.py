
import librosa
import numpy as np
import soundfile as sf
from pathlib import Path

# Wczytujemy drugie nagranie
plik = librosa.ex("libri1")
dzwiek, sr = librosa.load(plik, sr=None, duration=10)

# Obliczamy widmo i czestotliwosci
widmo = librosa.stft(dzwiek)
czestotliwosci = librosa.fft_frequencies(
    sr=sr, n_fft=2048
)

# Energia oryginalnego nagrania
energia_oryginal = np.sum(dzwiek ** 2)


def filtruj_gore(widmo, czestotliwosci, granica, liczba_probek):

    maska = czestotliwosci > granica

    widmo_filtrowane = widmo.copy()
    widmo_filtrowane[maska, :] = 0

    wynik = librosa.istft(
        widmo_filtrowane,
        length=liczba_probek
    )

    return wynik



def filtruj_pasmo(widmo, czestotliwosci, dol, gora, liczba_probek):

    maska = (czestotliwosci < dol) | (czestotliwosci > gora)

    widmo_filtrowane = widmo.copy()
    widmo_filtrowane[maska, :] = 0

    wynik = librosa.istft(
        widmo_filtrowane,
        length=liczba_probek
    )

    return wynik



# Folder na wyniki
folder = Path(__file__).resolve().parent / "outputs"
folder.mkdir(exist_ok=True)

# Automatycznie sprawdzamy kilka granic
for granica in [3000, 4000, 5000, 7000]:
    dzwiek_filtrowany = filtruj_gore(
        widmo,
        czestotliwosci,
        granica,
        len(dzwiek)
    )

    energia_filtrowany = np.sum(dzwiek_filtrowany ** 2)

    procent = (energia_filtrowany / energia_oryginal) * 100

    nazwa = f"libri1_do_{granica}Hz.wav"

    sf.write(folder / nazwa, dzwiek_filtrowany, sr)

    print(f"Pasmo 0-{granica} Hz: {procent:.2f}% energii")


# Filtruje pasmo od 500 do 4000 Hz
dzwiek_pasmo = filtruj_pasmo(
    widmo,
    czestotliwosci,
    500,
    4000,
    len(dzwiek)
)

# Obliczam procent pozostalej energii
energia_pasmo = np.sum(dzwiek_pasmo ** 2)
procent_pasmo = (energia_pasmo / energia_oryginal) * 100

# Zapisujemy wynik
sf.write(folder / "libri1_pasmo_500_4000Hz.wav", dzwiek_pasmo, sr)

print(f"Pasmo 500-4000 Hz: {procent_pasmo:.2f}% energii")
