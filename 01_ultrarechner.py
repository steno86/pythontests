# Ultrarechner v0.1

print()
print("Dies ist der Ultrarechner 0.1")
print("Ich zeige dir was ich mit zwei Zahlen")
print("alles kann!")
print()

zahl_1 = input("Bitte gib die erste Zahl ein: ")
print("Vielen Dank!")
print()

zahl_2 = input("Bitte gib nun die zweite Zahl ein: ")
print("Vielen Dank!")
print()

print("Ich rechne.....")
print()

print("Mit deinen Zahlen " + zahl_1 + " und " + zahl_2)
print("komme ich mit meiner Intelligenz auf folgende Ergebnisse:")
print()
addition = float(zahl_1) + float(zahl_2)
subtraktion = float(zahl_1) - float(zahl_2)
multiplikation = float(zahl_1) * float(zahl_2)
division = float(zahl_1) / float(zahl_2)

print(" " + str(zahl_1) + " plus " + str(zahl_2) + " ergibt " + str(addition))
print(" " + str(zahl_1) + " minus " + str(zahl_2) + " ergibt " + str(subtraktion))
print(" " + str(zahl_1) + " mal " + str(zahl_2) + " ergibt " + str(multiplikation))
print(" " + str(zahl_1) + " geteilt durch " + str(zahl_2) + " ergibt " + str(division))
print()

print("Ich hoffe ich konnte dir deine Fragen beantworten!")