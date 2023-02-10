class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, type):
        if species == 'mammal':
            self.mammals.append(type)
        elif species == 'fish':
            self.fishes.append(type)
        elif species == 'bird':
            self.birds.append(type)
        Zoo.__animals += 1

    def get_info(self, species):
        result = ''
        if species == 'mammal':
            result += f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}"
        elif species == 'fish':
            result += f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals}"
        elif species == 'bird':
            result += f"Birds in {self.zoo_name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}"
        return result


name_of_zoo = input()
zoo = Zoo(name_of_zoo)
number_of_animals = int(input())
for animal in range(number_of_animals):
    current_animal = input().split(' ')
    species = current_animal[0]
    type = current_animal[1]
    zoo.add_animal(species, type)

info = input()
print(zoo.get_info(info))
