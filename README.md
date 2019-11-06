# PTSZ

Practice and Theory of Job Scheduling (Praktyka i Teoria Szeregowania Zadań)



# Opis

P4 | rj | EDj
4 identyczne maszyny

n - liczba zadan
zbior zadan J = {J1, J2, ... , Jn}

opis zadania rj
pj - czas - processing time
rj - ready time
dj - due date - mozna przekroczyc ale jest kara


EDj - suma Dj - min tardiness - opoznienie

Dj = Cj - dj
Cj - completion time

## step 1
Wygenerować dane - generator instancji - na stronie jest opis
n
p1 r1 d1
p2 r2 d2
...
pn rn dn

n = 50, 100, 150, ... , 500 (10 rozmiarow) 

na kolejne zajecia

na OK byl opis mozna z tego skorzystac
podpowiedzi np Epj/4 jako czas ogolny i starac sie na podstawie tego wybierac rzeczy

## step 2
Weryfikator
tryb 1. instancje -> plik wynikowy

plik wynikowy:
EDj
J1.1 J1.2 J1.3
J2.1 J2.2 ...
...
J4.1 ...

np wektor
0
2 6
1 4
3 5
8

weryfikator ma cel zeby wyliczyc na podstawie wygenerowanych zadan

tworzymy sztuczne pliki wynikowe z jakas sekwencja (moze byc po prostu po kolei)
i sprawdzamy czy dane uszeregowanie daje odpowiedni wynik kosztu

tryb 2.
instancja, algorytm -> plik wynikowy


## Algorytm Listowy:
idee:
Shortest Processing Time
Longest Processing Time


1. Generator
2. Weryfikator
3. Algorytm listowy
4. Algorytm jakis heurystyczny
