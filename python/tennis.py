# -*- coding: utf-8 -*-
from score import Score


class TennisGame1:

    def __init__(self, player_1_name, player_2_name):
        self.player_1 = Player(player_1_name)
        self.player_2 = Player(player_2_name)
        self.current_score = None

    def won_point(self, player_name):
        if player_name == self.player_1.name:
            self.player_1.won_point()
        else:
            self.player_2.won_point()

    def score(self):
        self.current_score = Score.create_score(self.player_1, self.player_2)
        return self.current_score.print_score()


class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def won_point(self):
        self.points += 1
