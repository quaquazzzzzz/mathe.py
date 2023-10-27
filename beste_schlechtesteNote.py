# Zuerst definieren wir unsere Listen mit den Noten
mathematik = [80, 85, 90, 78, 92, 88, 76, 89, 95, 82]
physik = [75, 88, 82, 79, 91, 86, 77, 90, 94, 81]
chemie = [70, 84, 88, 76, 89, 82, 74, 87, 92, 79]

# Dann denken wir darüber nach, wie wir die beste Note in Mathematik finden können
# Eine Möglichkeit wäre, die Liste zu sortieren und das letzte Element auszuwählen
# Aber das könnte ineffizient sein, besonders wenn die Liste sehr groß ist
# Also verwenden wir die max() Funktion von Python, die uns direkt den höchsten Wert gibt

beste_mathematik = max(mathematik)
print("Beste Mathematik Note:", beste_mathematik)  # Nur zur Überprüfung

# Ähnlich können wir die min() Funktion verwenden, um die niedrigste Note zu finden
schlechteste_mathematik = min(mathematik)
print("Schlechteste Mathematik Note:", schlechteste_mathematik)  # Nur zur Überprüfung

# Wir wiederholen das gleiche für Physik
beste_physik = max(physik)
print("Beste Physik Note:", beste_physik)

schlechteste_physik = min(physik)
print("Schlechteste Physik Note:", schlechteste_physik)

# Und dann für Chemie
beste_chemie = max(chemie)
print("Beste Chemie Note:", beste_chemie)

schlechteste_chemie = min(chemie)
print("Schlechteste Chemie Note:", schlechteste_chemie)

# Jetzt möchten wir die besten und schlechtesten Noten in Listen speichern
besten_noten = [beste_mathematik, beste_physik, beste_chemie]
schlechtesten_noten = [schlechteste_mathematik, schlechteste_physik, schlechteste_chemie]

print("\nZusammenfassung:")
print("Besten Noten:", besten_noten)
print("Schlechtesten Noten:", schlechtesten_noten)
