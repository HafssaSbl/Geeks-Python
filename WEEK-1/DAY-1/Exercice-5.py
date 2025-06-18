my_fav_numbers = {3, 7, 21}
print("Mes nombres préférés :", my_fav_numbers)


my_fav_numbers.add(42)
my_fav_numbers.add(88)
print("Après ajout de deux nombres :", my_fav_numbers)

my_fav_numbers.remove(88)
print("Après suppression du dernier nombre ajouté :", my_fav_numbers)

friend_fav_numbers = {5, 12, 42}
print("Les nombres préférés de mon ami :", friend_fav_numbers)

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print("Nos nombres préférés (sans doublons) :", our_fav_numbers)
