class Score:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self._player_in_advantage = None

    @staticmethod
    def create_score(player_1, player_2):
        if player_1.points == player_2.points:
            return TieScore(player_1, player_2)

        if player_1.points >= 4 or player_2.points >= 4:
            if abs(player_1.points - player_2.points) >= 2:
                return GameOver(player_1, player_2)
            else:
                return AdvantageScore(player_1, player_2)

        return Score(player_1, player_2)

    @property
    def player_in_advantage(self):
        if self.player_1.points == self.player_2.points:
            self._player_in_advantage = None

        elif self.player_1.points > self.player_2.points:
            self._player_in_advantage = self.player_1

        elif self.player_1.points < self.player_2.points:
            self._player_in_advantage = self.player_2

        return self._player_in_advantage

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
        return f"Win for {self.player_in_advantage.name}"


class AdvantageScore(Score):
    def print_score(self):
        return f"Advantage {self.player_in_advantage.name}"
