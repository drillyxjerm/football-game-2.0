import random

class Team:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.turnover = False

    def run_play(self):
        # Simulate a running play with a moderate chance of scoring
        if random.random() < 0.5:
            self.score += 7  # Touchdown

    def pass_play(self):
        # Simulate a passing play with a higher chance of scoring but also a risk of turnover
        pass_success = random.random()
        if pass_success < 0.3:
            self.score += 7  # Touchdown
        elif pass_success > 0.8:
            self.turnover = True  # Turnover occurred

class FootballGame:
    def __init__(self, player_team_name):
        self.player_team = Team(player_team_name)
        self.computer_team = Team("Computer Team")

    def play_turn(self):
        # Player's turn
        self.player_team.turnover = False  # Reset turnover status
        player_choice = input("Choose your play (run/pass): ").lower()
        if player_choice == "run":
            self.player_team.run_play()
        elif player_choice == "pass":
            self.player_team.pass_play()
            if self.player_team.turnover:
                print("Turnover! The computer will now play.")
                self.computer_team.run_play()  # Computer gets a chance to score after turnover
                return  # End player's turn

        # Computer's turn
        self.computer_team.turnover = False  # Reset turnover status
        if random.random() < 0.5:
            self.computer_team.run_play()
        else:
            self.computer_team.pass_play()
            if self.computer_team.turnover:
                print("Computer turnover! Your turn again.")
                return  # End computer's turn

    def display_scores(self):
        print(f"{self.player_team.name}: {self.player_team.score} | {self.computer_team.name}: {self.computer_team.score}")

def main():
    player_team_name = input("Enter your team name: ")
    game = FootballGame(player_team_name)

    print(f"Welcome to the Football Game! {game.player_team.name} vs. {game.computer_team.name}")

    for quarter in range(1, 5):
        print(f"\nQuarter {quarter}:")
        game.play_turn()
        game.display_scores()

    print("\nGame Over!")
    game.display_scores()

if __name__ == "__main__":
    main()
