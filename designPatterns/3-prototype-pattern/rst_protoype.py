from prototype_1 import Prototype
from copy import deepcopy


class Knight(Prototype):
    def __init__(self, unit_type, level):
        self.unit_type = unit_type
        self.level = level

        filename = "{}_{}.dat".format(self.unit_type, level)

        with open(filename, 'r') as parameter_file:
            lines = parameter_file.read().split("\n")
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[4]

    def __str__(self):
        return "Type: {0}\n" \
               "Level: {1}\n" \
               "Life: {2}\n" \
               "Speed: {3}\n" \
               "Attack Power: {4}\n" \
               "Attack Range: {5}\n" \
               "Weapon: {6}".format(self.unit_type, self.level,
                                    self.life, self.speed,
                                    self.attack_power, self.attack_range,
                                    self.weapon)

    def clone(self):
        return deepcopy(self)


class Archer(Knight):
    pass


class Barracks(object):
    def __init__(self):
        self.units = {
            "Knight": {
                1: Knight("Knight", 1),
                2: Knight("Knight", 2)
                },
            "Archer": {
                1: Archer("Archer", 1),
                2: Archer("Archer", 2)
                }
            }

    def build_unit(self, unit_type, level):
        return self.units[unit_type][level].clone()


if __name__ == "__main__":
    barracks = Barracks()
    knight1 = barracks.build_unit("Knight", 2)
    archer1 = barracks.build_unit("Archer", 1)
    print("[knight1] {}".format(knight1))
    print("[archer1] {}".format(archer1))
