# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 15:35:22 2016

@author: Philip
"""


class Player():
# Generic class for agent in normal-form game
    def __init__(self,name,actions=None) :
        self.name = name

class Game():
# Generic class for normal-form game

    def __init__(self,players,actions,payoffs) :
    # players: length-n list of players
    # actions: length-n list or dict of lists of actions
    # payoffs: exact structure TBD
        if len(players)
        self.players = players
        self.actions = actions
        self.payoffs = payoffs