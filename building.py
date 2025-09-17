class Building:
    def __init__(self, number_of_floors, number_of_elevators):
        self.structure = []
        self.number_of_floors = number_of_floors
        self.number_of_elevators = number_of_elevators

    def build(self):
        self.structure = \
        [
            "-----ROOF-----",
            "-----GROUND----"
        ]

        temp_floors = self.number_of_floors

        while temp_floors:
            level = '|L' + f'{temp_floors}'.center(3) + '|' + self.number_of_elevators * f'|    |'
            self.structure.insert(-1,level)
            temp_floors -= 1

    def show(self):
        print("\n".join(self.structure))




if __name__ == "__main__":
    my_home = Building(10, 2)
    my_home.build()
    my_home.show()