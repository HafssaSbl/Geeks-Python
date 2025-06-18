basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")

basket.remove("Blueberries")

basket.append("Kiwi")

basket.insert(0, "Apples")

count_apples = basket.count("Apples")
print(f"Le nombre d'apparitions de 'Apples' est : {count_apples}")

basket.clear()

print("État final de la liste :", basket)
