# base class
class Musician:
    def __init__(self, name):
        self.name = name


# derived class
class Guitarist(Musician):
    def __init__(self, name="unknown", jump=0):
        self.name = name
        self.jump = jump

    def __str__(self):
        return self.name


class Bassist(Musician):
    pass


class Drummer(Musician):
    pass
