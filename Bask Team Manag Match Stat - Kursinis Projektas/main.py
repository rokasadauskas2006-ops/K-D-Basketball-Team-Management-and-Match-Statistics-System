from factory.person_factory import PersonFactory
from models.team import Team
from models.match import Match
from models.stats_record import StatsRecord
from services.file_manager import FileManager


def main():
    # Sukuriu coach su factory design pattern
    coach = PersonFactory.create_person("coach", "Tomas Masiulis", 39, 4)

    # Sukuriu komandą
    team = Team("Zalgiris", coach)

    # Sukuriu žaidėjus naudodamas Factory Pattern
    p1 = PersonFactory.create_person("player", "Nigel Williams-Goss", 30, 1, "Guard", 191)
    p2 = PersonFactory.create_person("player", "Sylvain Francisco", 28, 3, "Guard", 185)
    p3 = PersonFactory.create_person("player", "Azuolas Tubelis", 24, 10, "Forward", 208)
    p4 = PersonFactory.create_person("player", "Laurynas Birutis", 27, 15, "Center", 213)
    p5 = PersonFactory.create_person("player", "Edgaras Ulanovas", 34, 92, "Forward", 199)

    # Pridedu žaidėjus į komandą
    team.add_player(p1)
    team.add_player(p2)
    team.add_player(p3)
    team.add_player(p4)
    team.add_player(p5)

    # Parodau komandos informaciją
    print("=== TEAM INFORMATION ===")
    team.show_team()

    # Išsaugau komandos duomenis į JSON failą
    FileManager.save_to_file(team.to_dict(), "team.json")
    print("\nTeam saved to team.json")

    # Užkraunu duomenis iš failo ir parodau
    loaded_data = FileManager.load_from_file("team.json")
    print("\n=== LOADED DATA FROM FILE ===")
    print(loaded_data)

    # Sukuriu antrą trenerį ir komandą
    coach2 = PersonFactory.create_person("coach", "Giedrius Zibenas", 40, 6)

    # Sukuriu antrą komandą
    team2 = Team("Rytas", coach2)

    # Sukuriu žaidimą tarp dviejų komandų
    match = Match(team, team2)

    # Nustatau rezultatus
    match.set_score(85, 78)

    # Pridedu statistiką
    stat1 = StatsRecord(p1, 18, 6, 4)
    stat2 = StatsRecord(p2, 16, 5, 3)
    stat3 = StatsRecord(p3, 12, 2, 7)
    stat4 = StatsRecord(p4, 11, 1, 8)
    stat5 = StatsRecord(p5, 14, 4, 5)

    match.add_stat(stat1)
    match.add_stat(stat2)
    match.add_stat(stat3)
    match.add_stat(stat4)
    match.add_stat(stat5)

    # Parodau žaidimo informaciją
    print("\n=== MATCH INFORMATION ===")
    match.show_match()


if __name__ == "__main__":
    main()