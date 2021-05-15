# -*- coding: utf-8 -*-

class TennisGame1:

    def __init__(self, player_1_name, player_2_name):
        self.player_1_name = player_1_name
        self.player_2_name = player_2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == self.player_1_name:
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        score_data = self._compute_score()
        return self._print_score(score_data)

    def _compute_score(self):
        score_data = {}

        if self.p1points == self.p2points:
            score_data['player_in_advantage'] = None
        elif self.p1points > self.p2points:
            score_data['player_in_advantage'] = self.player_1_name
        else:
            score_data['player_in_advantage'] = self.player_2_name

        if self.p1points >= 4 or self.p2points >= 4:
            score_data['advantage_mode'] = True
            if abs(self.p1points - self.p2points) >= 2:
                score_data['game_over'] = True

        return score_data

    def _print_score(self, score_data):
        if score_data.get('game_over'):
            return f"Win for {score_data['player_in_advantage']}"
        if score_data.get('advantage_mode') \
                and score_data.get('player_in_advantage'):
            return f"Advantage {score_data['player_in_advantage']}"

        if not score_data.get('player_in_advantage'):
            return self._convert_tie_points(self.p1points)
        return f'{self._convert_tennis_points(self.p1points)}-' \
               f'{self._convert_tennis_points(self.p2points)}'

    def _convert_tie_points(self, points):
        if points < 3:
            return f"{self._convert_tennis_points(points)}-All"
        else:
            return "Deuce"

    @staticmethod
    def _convert_tennis_points(points):
        return {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
        }[points]
