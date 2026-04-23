from models.person import Person


class Coach(Person):
    def __init__(self, name, age, experience):
        super().__init__(name, age)
        self.experience = experience

    def get_info(self):
        return f"Coach: {self.name}, Age: {self.age}, Experience: {self.experience} years"