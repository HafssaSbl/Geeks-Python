import random

def get_random_temp(season=None):
    """
    Retourne une température flottante selon la saison.
    Si season est None, prend une température aléatoire entre -10 et 40.
    """
    if season == "winter":
        return random.uniform(-10, 10)
    elif season == "spring":
        return random.uniform(10, 20)
    elif season == "summer":
        return random.uniform(20, 40)
    elif season == "autumn":
        return random.uniform(10, 20)
    else:
        return random.uniform(-10, 40)

def determine_season(month):
    if month in [12, 1, 2]:
        return "winter"
    elif month in [3, 4, 5]:
        return "spring"
    elif month in [6, 7, 8]:
        return "summer"
    elif month in [9, 10, 11]:
        return "autumn"
    else:
        return None

def main():
    try:
        month = int(input("Entrez le numéro du mois (1-12) : "))
        if month < 1 or month > 12:
            print("Mois invalide. Je vais choisir une température aléatoire.")
            season = None
        else:
            season = determine_season(month)
    except ValueError:
        print("Entrée invalide. Je vais choisir une température aléatoire.")
        season = None

    temp = get_random_temp(season)
    print(f"The temperature right now is {temp:.1f} degrees Celsius.")

    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temp <= 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 < temp <= 23:
        print("Nice weather.")
    elif 23 < temp <= 32:
        print("A bit warm, stay hydrated.")
    else:  # temp > 32
        print("It’s really hot! Stay cool.")

if __name__ == "__main__":
    main()
