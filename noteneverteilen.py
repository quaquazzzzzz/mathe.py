from collections import Counter

# Angenommen, dies sind die Noten für Mathematik
mathematik = [80, 85, 80, 90, 87, 85, 90, 80, 88, 85]

# Verwenden von Counter, um die Häufigkeit jeder Note zu zählen
noten_haeufigkeit = Counter(mathematik)

# Die Verteilung der Noten anzeigen
for note, haeufigkeit in sorted(noten_haeufigkeit.items()):
    print(f"Note {note}: {haeufigkeit} mal")
