class Match:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.score1 = 0
        self.score2 = 0
        self.stats = []

    def set_score(self, score1, score2):
        self.score1 = score1
        self.score2 = score2

    def add_stat(self, stat_record):
        self.stats.append(stat_record)

    def show_match(self):
        print(f"{self.team1.name} vs {self.team2.name}")
        print(f"Score: {self.score1} - {self.score2}")
        print("Player stats:")

        for stat in self.stats:
            print(stat.get_info())