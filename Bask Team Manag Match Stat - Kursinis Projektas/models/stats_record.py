class StatsRecord:
    def __init__(self, player, points, assists, rebounds):
        self.player = player
        self.points = points
        self.assists = assists
        self.rebounds = rebounds

    def get_info(self):
        return (
            f"{self.player.name}: "
            f"{self.points} pts, "
            f"{self.assists} ast, "
            f"{self.rebounds} reb"
        )
