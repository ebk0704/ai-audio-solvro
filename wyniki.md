
# Eksperymenty AI Audio

## Cel
Zbadanie, jak usuwanie wybranych czestotliwosci
wplywa na brzmienie i zrozumialosc ludzkiej mowy.

## Nagranie
10-sekundowy fragment przykladowego nagrania
mowy z biblioteki librosa (LibriSpeech).

## Eksperymenty

| Zachowane pasmo | Obserwacja |
|---|---|
| 0-3000 Hz | Glos stlumiony, mniej zrozumialy |
| 0-4000 Hz | Prawie tak dobry jak przy 5000 Hz |
| 0-5000 Hz | Lepsze brzmienie niz przy 4000 Hz |
| 0-7000 Hz | Bardzo podobny do oryginalu |
| 300-11025 Hz | Glos mniej basowy, nadal zrozumialy |
| 500-11025 Hz | Nadal zrozumialy |
| 500-5000 Hz | Nadal zrozumialy |
| 500-4000 Hz | Nadal zrozumialy |


## Pomiary energii

| Nagranie | Zachowane pasmo | Pozostala energia | Zrozumialosc |
|---|---|---|---|
| libri1 | 0-7000 Hz | 99,99% | Prawie identyczne z oryginałem |
| libri1 | 500-4000 Hz | 13,51% | Slowa zrozumiale |
| libri2 | 0-7000 Hz | 99,99% | Prawie identyczne z oryginalem |
| libri2 | 500-4000 Hz | 34,98% | Slowa zrozumiale |

## Wstepne wnioski

1. Wysokie czestotliwosci wplywaja na wyraznosc mowy.
2. Niskie czestotliwosci silnie wplywaja na
   barwe glosu i energie sygnalu.
3. Znaczna redukcja energii nie musi oznaczac
   utraty zrozumialosci wypowiedzi.
4. Usuniecie czestotliwosci powyzej 7000 Hz
   mialo niewielki wplyw na badane nagranie.
5. Ten sam filtr pozostawia rozny procent energii
   w roznych nagraniach.
6. W obu badanych probkach pasmo 500-4000 Hz
   wystarczylo do zrozumienia wypowiadanych slow.
7. Procent zachowanej energii nie jest rownowazny
   procentowi zachowanej informacji o mowie.

## Ograniczenia

Eksperymenty wykonano na jednym nagraniu.
Zrozumialosc oceniano subiektywnie podczas odsluchu.
Wnioski wymagaja sprawdzenia na innych probkach mowy.


## Co mozna odczytac ze spektrogramu?

Spektrogram pokazuje, jak zmienia sie sila skladowych
czestotliwosciowych dzwieku w czasie.

Mozemy zaobserwowac:
- fragmenty mowy i przerwy,
- dominujace zakresy czestotliwosci,
- zmiany rozkladu czestotliwosci w czasie,
- skutki usuniecia wybranych skladowych sygnalu.

## Czego nie mozna wiarygodnie odczytac?

Na podstawie samego spektrogramu nie mozemy
wiarygodnie ustalic:
- dokladnych wypowiadanych slow,
- tozsamosci osoby mowiacej,
- dokladnego przebiegu oryginalnej fali dzwiekowej,
  jesli nie znamy informacji o fazie.

Nie mozemy tez ocenic zrozumialosci mowy
wylacznie na podstawie kolorow spektrogramu.
Dlatego nasze hipotezy sprawdzalismy przez odsluch.
