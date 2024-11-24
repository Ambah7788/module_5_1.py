class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1:
            return f"Этаж {new_floor} не существует. Пожалуйста, выберите этаж от 1 до {self.number_of_floors}."
        elif new_floor > self.number_of_floors:
            return f"Этаж {new_floor} не существует. Пожалуйста, выберите этаж от 1 до {self.number_of_floors}."
        else:
            return f"Вы находитесь на этаже {new_floor} в доме '{self.name}'."

my_house = House("Солнечный дом", 5)

result = my_house.go_to(3)
print(result)

result_invalid = my_house.go_to(6)
print(result_invalid) 