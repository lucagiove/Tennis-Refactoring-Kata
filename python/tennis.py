# -*- coding: utf-8 -*-

class TennisGame1:

    def __init__(self, player_1_name, player_2_name):
        self.player1Name = player_1_name
        self.player2Name = player_2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == self.player1Name:
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        result = ""
        if self.p1points == self.p2points:
            result = self._convert_tie_points_to_tennis_score(self.p1points)
        elif self.p1points >= 4 or self.p2points >= 4:
            minus_result = self.p1points - self.p2points
            if minus_result == 1:
                result = "Advantage " + self.player1Name
            elif minus_result == -1:
                result = "Advantage " + self.player2Name
            elif minus_result >= 2:
                result = "Win for " + self.player1Name
            else:
                result = "Win for " + self.player2Name
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
