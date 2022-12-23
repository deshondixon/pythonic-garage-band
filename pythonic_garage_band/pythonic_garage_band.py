# inheritance vs composition
class Band:
    def __init__(self, musicians=False):
        self.musicians = musicians or []

    def __str__(self):
        musician_strings = []
        for musician in self.musicians:
            musician_strings.append(str(musician))
        return " ".join(musician_strings)

    def __repr__(self):
        return f"Band({self.name})"


# base class
class Musician:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Musician({self.name})"


# derived class
class Guitarist(Musician):
    def __init__(self, name="unknown", jump=0):
        self.name = name
        self.jump = jump

    def __str__(self):
        return self.name

    def greet(self):
        return f"The name's {self.name}. Pleasure."

    def __repr__(self):
        return f"Guitarist({self.name})"


class Bassist(Musician):
    def __init__(self, name="unknown", jump=0):
        self.name = name
        self.jump = jump

    def __str__(self):
        return self.name

    def greet(self):
        return f"The name's {self.name}. Pleasure."

    def __repr__(self):
        return f"Bassist({self.name})"


class Drummer(Musician):
    def __init__(self, name="unknown", jump=0):
        self.name = name
        self.jump = jump

    def __str__(self):
        return self.name

    def greet(self):
        return f"The name's {self.name}. Pleasure."

    def __repr__(self):
        return f"Drummer({self.name})"
