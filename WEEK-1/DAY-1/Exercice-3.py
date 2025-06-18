
mon_nom = "Hafssa"  


nom_utilisateur = input("Quel est ton prénom ? ")

if nom_utilisateur.strip().lower() == mon_nom.lower():
    print("Incroyable ! On a le même prénom ! On est sûrement des âmes jumelles ")
else:
    print(f"Ah, {nom_utilisateur} ? Sympa, mais {mon_nom} reste quand même plus stylé ")
