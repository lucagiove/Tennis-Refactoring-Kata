class Score:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_in_advantage = None

    def compute_score(self):
        score_data = {}

        if self.player_1.points > self.player_2.points:
            score_data['player_in_advantage'] = self.player_1.name
            self.player_in_advantage = self.player_1.name
        else:
            score_data['player_in_advantage'] = self.player_2.name
            self.player_in_advantage = self.player_2.name

        if self.player_1.points >= 4 or self.player_2.points >= 4:
            score_data['advantage_mode'] = True
            if abs(self.player_1.points - self.player_2.points) >= 2:
                score_data['game_over'] = True

        return score_data

    def print_score(self, score_data):
        if score_data.get('advantage_mode') \
                and score_data.get('player_in_advantage'):
            return f"Advantage {score_data['player_in_advantage']}"

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
    def print_score(self, score_data):
        return self._convert_tie_points(self.player_1.points)

    def _convert_tie_points(self, points):
        if points < 3:
            return f"{self._convert_tennis_points(points)}-All"
        else:
            return "Deuce"


class GameOver(Score):
    def print_score(self, score_data):
        return f"Win for {score_data['player_in_advantage']}"


class AdvantageScore(Score):
    def print_score(self, score_data):
        return f"Advantage {self.player_in_advantage}"
