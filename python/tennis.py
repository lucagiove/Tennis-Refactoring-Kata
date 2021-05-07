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
            result = self._return_advantage_or_winner(self.p1points, self.p2points,
                                                      self.player_1_name, self.player_2_name)
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

    @staticmethod
    def _covert_intermediate_points_to_tennis_score(p1points, p2points):
        result = ""
        for i in range(1, 3):
            if i == 1:
                temp_score = p1points
            else:
                result += "-"
                temp_score = p2points
            result += {
                0: "Love",
                1: "Fifteen",
                2: "Thirty",
                3: "Forty",
            }[temp_score]
        return result

    @staticmethod
    def _return_advantage_or_winner(p1points, p2points, player_1_name, player_2_name):
        minus_result = p1points - p2points

        if minus_result == 1:
            result = "Advantage " + player_1_name
        elif minus_result == -1:
            result = "Advantage " + player_2_name
        elif minus_result >= 2:
            result = "Win for " + player_1_name
        else:
            result = "Win for " + player_2_name
        return result
