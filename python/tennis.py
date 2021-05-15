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
        result, score_data = self._compute_score()
        result = self._print_score(score_data, result)
        return result

    def _compute_score(self):
        score_data = {}
        result = None

        if self.p1points >= 4 or self.p2points >= 4:
            score_data['advantage_mode'] = True
            if self.p1points == self.p2points:
                score_data['player_in_advantage'] = False
            else:
                if self.p1points > self.p2points:
                    score_data['player_in_advantage'] = self.player_1_name
                else:
                    score_data['player_in_advantage'] = self.player_2_name
                if abs(self.p1points - self.p2points) >= 2:
                    score_data['game_over'] = True
        else:
            if self.p1points == self.p2points:
                score_data['player_in_advantage'] = False
        return result, score_data

    def _print_score(self, score_data, result):
        if score_data.get('game_over'):
            return self._return_winner(score_data['player_in_advantage'])
        if score_data.get('advantage_mode'):
            if score_data.get('player_in_advantage', None) is False:
                return self._convert_tie_points_to_tennis_score(self.p1points)
            return self._return_advantage(score_data['player_in_advantage'])
        else:
            if score_data.get('player_in_advantage', None) is False:
                return self._convert_tie_points_to_tennis_score(self.p1points)
            return self._covert_intermediate_points_to_tennis_score(self.p1points, self.p2points)

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
