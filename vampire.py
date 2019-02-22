class Vampire:
    """ A class about vampires"""

    coven = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.drank_blood_today = None
        self.in_coffin = None

    @classmethod
    def create(self, name, age):
        new_vampire = Vampire(name, age)
        Vampire.coven.append(new_vampire)
        return new_vampire

    def drink_blood(self):
        self.drank_blood_today = True
        return self.drank_blood_today

    @classmethod
    def sunrise(self):
        """sunrise, which removes from the coven any vampires who are out
        of their coffins or who haven't drank any blood in the last day"""
        for vampire in Vampire.coven:
            if self.drank_blood_today is False:
                Vampire.coven.remove(vampire)


bob = Vampire.create('Bob', 1001)
print(Vampire.coven)
print(bob.drink_blood())
