from models.person import Person


class Player(Person):
    def __init__(self, name, age, number, position, height):
        super().__init__(name, age)
        self.number = number
        self.position = position
        self.height = height

    def get_info(self):
        return f"Player: {self.name}, Age: {self.age}, Number: {self.number}, Position: {self.position}, Height: {self.height} cm"
