# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Person:
    def __init__(self, city_population: int, room_num: int):
        self.city_popultaion = city_population
        self.room_num = room_num

    def get_person_room(self):
        return self.room_num

    def get_city_population(self):
        return self.city_popultaion


# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.

if __name__ == '__main__':
    person = Person(650000, 8)
    print(person.get_city_population())
    print(person.get_person_room())

