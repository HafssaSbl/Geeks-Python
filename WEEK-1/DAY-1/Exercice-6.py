
mon_tuple = (1, 2, 3)
print("Tuple initial :", mon_tuple)

try:
    mon_tuple.append(4)  
except AttributeError as e:
    print("Erreur :", e)


print("Les tuples sont immuables : on ne peut pas modifier, ajouter ou supprimer leurs éléments.")

nouveau_tuple = mon_tuple + (4, 5)
print("Nouveau tuple (ajout indirect) :", nouveau_tuple)
