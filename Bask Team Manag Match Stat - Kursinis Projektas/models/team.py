class Team:
    def __init__(self, name, coach):
        self.name = name
        self.coach = coach
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player_number):
        for player in self.players:
            if player.number == player_number:
                self.players.remove(player)
                return "Player removed"
        return "Player not found"

    def show_team(self):
        print(f"Team: {self.name}")
        print(self.coach.get_info())
        print("Players:")

        for player in self.players:
            print(player.get_info())

    def to_dict(self):
        return {
            "name": self.name,
            "coach": {
                "name": self.coach.name,
                "age": self.coach.age,
                "experience": self.coach.experience
            },
            "players": [
                {
                    "name": player.name,
                    "age": player.age,
                    "number": player.number,
                    "position": player.position,
                    "height": player.height
                }
                for player in self.players
            ]
        }