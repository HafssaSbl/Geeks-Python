class Cat():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    

One_cat = Cat("mimi",12)
Two_Cat = Cat("koko",5)
Three_Cat = Cat("SoSo",6)

def find_oldest_cat(One_cat, Two_Cat, Three_Cat):
    oldest = One_cat
    if Two_Cat.age > oldest.age:
        oldest = cat2
    if Three_Cat.age > oldest.age:
        oldest = cat3
    return oldest

oldest_cat = find_oldest_cat(One_cat, Two_Cat, Three_Cat)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")
