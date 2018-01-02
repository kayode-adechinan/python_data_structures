# finding common interests

josh_interests = ["painting", "travel", "eating"]

paula_interests = ["painting", "reading", "writing", "travel"]


common_interests = set(josh_interests).intersection(set(paula_interests))

print(common_interests)


# finding common address

class Human:
    def __init__(self, name, address):
        self.name =  name
        self.address = address

    def __str__(self):
        return self.name  + self.address


fox_river_men = [Human(name="richard malone", address="new york"), Human(name="robert", address="oregon")]
print(fox_river_men)



