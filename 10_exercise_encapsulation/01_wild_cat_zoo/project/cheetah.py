from project.animal import Animal


class Cheetah(Animal):
    MONE_FOR_CARE = 60

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, Cheetah.MONE_FOR_CARE)
