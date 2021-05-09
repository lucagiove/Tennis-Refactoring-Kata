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
        if self.p1points == self.p2points:
            result = self._convert_tie_points_to_tennis_score(self.p1points)
        elif self.p1points >= 4 or self.p2points >= 4:
            if self.p1points > self.p2points:
                player_in_advantage = self.player_1_name
            else:
                player_in_advantage = self.player_2_name
            if abs(self.p1points - self.p2points) >= 2:
                result = self._return_winner(player_in_advantage)
            else:
                result = self._return_advantage(player_in_advantage)

        else:
            result = self._covert_intermediate_points_to_tennis_score(self.p1points, self.p2points)
        return result

    @staticmethod
    def _convert_tie_points_to_tennis_score(points1):
        return {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
        }.get(points1, "Deuce")

    def _covert_intermediate_points_to_tennis_score(self, p1points, p2points):
        result = f'{self._convert_points_to_tennis_score(p1points)}-' \
                 f'{self._convert_points_to_tennis_score(p2points)}'
        return result

    @staticmethod
    def _convert_points_to_tennis_score(points):
        return {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
        }[points]

    @staticmethod
    def _return_advantage(player_name):
        return "Advantage " + player_name

    @staticmethod
    def _return_winner(player_name):
        return "Win for " + player_name
