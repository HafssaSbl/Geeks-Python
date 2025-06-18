sandwich_orders = [
    "Tuna sandwich", 
    "Pastrami sandwich", 
    "Avocado sandwich", 
    "Pastrami sandwich", 
    "Egg sandwich", 
    "Chicken sandwich", 
    "Pastrami sandwich"
]

print("Désolé, le pastrami est en rupture de stock.")

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"Je prépare votre {sandwich.lower()}.")
    finished_sandwiches.append(sandwich)

print("\nListe des sandwichs préparés :")
for sandwich in finished_sandwiches:
    print(f"J'ai préparé votre {sandwich.lower()}.")
