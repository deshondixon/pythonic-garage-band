# inheritance vs composition
class Band:
    def __init__(self, name="unknown", members=False):
        self.name = name
        self.members = members or []

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"({self.name})"

    def play_solos(self):
        return [member.play_solo() for member in self.members]


# base class
class Musician:
    def __init__(self, name, instrument, musician_type, solo):
        self.name = name
        self.instrument = instrument
        self.musician_type = musician_type
        self.solo = solo

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"{self.musician_type} instance. Name = {self.name}"

    def get_instrument(self):
        return f"{self.instrument}"

    def play_solo(self):
        return f"{self.solo}"


# derived class
class Guitarist(Musician):
    def __init__(self, name="unknown"):
        super().__init__(name, "guitar", "Guitarist", "face melting guitar solo")


class Bassist(Musician):
    def __init__(self, name="unknown"):
        super().__init__(name, "bass", "Bassist", "bom bom buh bom")


class Drummer(Musician):
    def __init__(self, name="unknown"):
        super().__init__(name, "drums", "Drummer", "rattle boom crash")
