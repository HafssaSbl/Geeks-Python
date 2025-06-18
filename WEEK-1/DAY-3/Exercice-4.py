class Zoo():
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
    
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print("Animals in the zoo:")
        for animal in self.animals:
            print("-", animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
       
        self.animals.sort()
        grouped = {}

        for animal in self.animals:
            letter = animal[0].upper()
            if letter not in grouped:
                grouped[letter] = [animal]
            else:
                grouped[letter].append(animal)

        self.animal_groups = grouped

    def get_groups(self):
        print("Grouped animals:")
        for letter, group in self.animal_groups.items():
            print(f"{letter}: {group}")