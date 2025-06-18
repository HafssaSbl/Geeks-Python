
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", 
                   "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

print("Désolé, nous sommes en rupture de Pastrami sandwich.")


while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")


finished_sandwiches = []


while sandwich_orders:
    sandwich = sandwich_orders.pop(0) 
    print(f"Je prépare votre {sandwich.lower()}.")
    finished_sandwiches.append(sandwich)


print("\n Tous les sandwiches ont été préparés :")
for sandwich in finished_sandwiches:
    print(f"👉 I made your {sandwich.lower()}")
