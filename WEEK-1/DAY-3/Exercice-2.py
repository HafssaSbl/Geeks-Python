class Dog():
    def __init__(self,name,height):
        self.name = name
        self.height = height
    
    def dark():
        print(" goes woof!")
    
    def jump():
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height} cm high!")

davids_dog = Dog("hihi",52)
sarahs_dog = Dog("hoho",60)

print(f"{davids_dog.name} is {davids_dog.height} cm tall.")
davids_dog.bark()
davids_dog.jump()

print(f"{sarahs_dog.name} is {sarahs_dog.height} cm tall.")
sarahs_dog.bark()
sarahs_dog.jump()