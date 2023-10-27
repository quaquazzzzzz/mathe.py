mathematik = [80, 85, 90, 78, 92, 88, 76, 89, 95, 82]
physik = [75, 88, 82, 79, 91, 86, 77, 90, 94, 81]
chemie = [70, 84, 88, 76, 89, 82, 74, 87, 92, 79]

# Summe der Noten in Mathematik berechnen
summe_mathematik = sum(mathematik)

# Anzahl der Noten in Mathematik
anzahl_mathematik = len(mathematik)

# Durchschnitt berechnen
durchschnitt_mathematik = summe_mathematik / anzahl_mathematik

print("Durchschnitt in Mathematik:", durchschnitt_mathematik)

# Für Physik
summe_physik = sum(physik)
anzahl_physik = len(physik)
durchschnitt_physik = summe_physik / anzahl_physik
print("Durchschnitt in Physik:", durchschnitt_physik)

# Für Chemie
summe_chemie = sum(chemie)
anzahl_chemie = len(chemie)
durchschnitt_chemie = summe_chemie / anzahl_chemie
print("Durchschnitt in Chemie:", durchschnitt_chemie)

durchschnitte = [durchschnitt_mathematik, durchschnitt_physik, durchschnitt_chemie]
print("Durchschnitte:", durchschnitte)
