family = {}

n = int(input("Combien de membres dans la famille ? "))

names = input("Noms des membres, séparés par des virgules : ").split(',')
ages = input("Âges des membres, séparés par des virgules : ").split(',')


names = [name.strip() for name in names]
ages = [int(age.strip()) for age in ages]

for i in range(n):
    family[names[i]] = ages[i]

total_cost = 0

for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    print(f"{name.title()} doit payer ${price}")
    total_cost += price

print(f"Coût total pour la famille : ${total_cost}")
