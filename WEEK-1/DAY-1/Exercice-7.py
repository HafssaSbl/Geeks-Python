
fruits = ["pomme", "banane", "orange"]
print("Liste initiale :", fruits)


fruits.append("kiwi")
print("Après ajout avec append :", fruits)


fruits.insert(0, "mangue")
print("Après insertion avec insert :", fruits)


fruits.remove("banane")
print("Après suppression avec remove :", fruits)


compteur_oranges = fruits.count("orange")
print("Nombre de fois que 'orange' apparaît :", compteur_oranges)


fruits.clear()
print("Après clear (liste vide) :", fruits)
