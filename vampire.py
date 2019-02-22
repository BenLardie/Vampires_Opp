class Vampire:
    """ A class about vampires"""

    coven = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.drank_blood_today = False
        self.in_coffin = False

    @classmethod
    def create(self, name, age):
        new_vampire = Vampire(name, age)
        Vampire.coven.append(new_vampire)
        return new_vampire

    def drink_blood(self):
        self.drank_blood_today = True
        return self.drank_blood_today

    @classmethod
    def sunrise(cls):
        """sunrise, which removes from the coven any vampires who are out
        of their coffins or who haven't drank any blood in the last day"""
        for self in Vampire.coven:
            if self.drank_blood_today is False and self.in_coffin is False:
                Vampire.coven.remove(self)
                return Vampire.coven

    @classmethod
    def sunset(cls):
        for vampire in Vampire.coven:
            Vampire.drank_blood_today = False
            Vampire.in_coffin = False

    def go_home(self):
        self.in_coffin = True


bob = Vampire.create('Bob', 1001)
judy = Vampire.create('Judy', 2001)
print(Vampire.coven)
print(bob.drink_blood())
Vampire.sunrise()
print(Vampire.coven)
Vampire.sunset()
Vampire.sunrise()
print(Vampire.coven)
