from models.player import Player
from models.coach import Coach


class PersonFactory:
    @staticmethod
    def create_person(person_type, *args):
        if person_type == "player":
            return Player(*args)
        elif person_type == "coach":
            return Coach(*args)
        else:
            return None