class Score:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_in_advantage = None

    def compute_score(self):
        if self.player_1.points > self.player_2.points:
            self.player_in_advantage = self.player_1.name
        else:
            self.player_in_advantage = self.player_2.name

    def print_score(self):
        return f'{self._convert_tennis_points(self.player_1.points)}-' \
               f'{self._convert_tennis_points(self.player_2.points)}'

    @staticmethod
    def _convert_tennis_points(points):
        return {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
        }[points]


class TieScore(Score):
    def print_score(self):
        return self._convert_tie_points(self.player_1.points)

    def _convert_tie_points(self, points):
        if points < 3:
            return f"{self._convert_tennis_points(points)}-All"
        else:
            return "Deuce"


class GameOver(Score):
    def print_score(self):
        return f"Win for {self.player_in_advantage}"


class AdvantageScore(Score):
    def print_score(self):
        return f"Advantage {self.player_in_advantage}"
