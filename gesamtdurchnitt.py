#Listen
mathematik = [80, 85, 90, 78, 92, 88, 76, 89, 95, 82]
physik = [75, 88, 82, 79, 91, 86, 77, 90, 94, 81]
chemie = [70, 84, 88, 76, 89, 82, 74, 87, 92, 79]

# Zuerst, die Summe jeder Fachliste wird berechnet
summe_mathematik = sum(mathematik)
summe_physik = sum(physik)
summe_chemie = sum(chemie)

gesamtsumme = summe_mathematik + summe_physik + summe_chemie

# Jetzt teilen wir die Gesamtsumme durch die Gesamtzahl der Noten
# Da jeder Fachliste 10 Noten enthält, gibt es insgesamt 30 Noten
gesamtdurchschnitt = gesamtsumme / 30

print("Gesamtdurchschnittsnote:", gesamtdurchschnitt)
