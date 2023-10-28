import sys
sys.path.append('C:\\Users\\annab\\27.10.23')

from durchschnitt_berechnen import mathematik, physik, chemie

print(mathematik)
print(physik)
print(chemie)

# Zählen, wie viele Schüler in Mathematik mindestens 90 Punkte haben
anzahl_90_mathematik = 0
for note in mathematik:
    if note >= 90:
        anzahl_90_mathematik += 1

# Zählen, wie viele Schüler in Physik mindestens 90 Punkte haben
anzahl_90_physik = 0
for note in physik:
    if note >= 90:
        anzahl_90_physik += 1

# Zählen, wie viele Schüler in Chemie mindestens 90 Punkte haben
anzahl_90_chemie = 0
for note in chemie:
    if note >= 90:
        anzahl_90_chemie += 1

# Speichern der Zahlen in einer neuen Liste
anzahl_90_liste = [anzahl_90_mathematik, anzahl_90_physik, anzahl_90_chemie]

print("Anzahl der Schüler mit mindestens 90 Punkten:", anzahl_90_liste)
