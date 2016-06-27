# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 15:35:22 2016

@author: Philip
"""
import numpy as np

class Player():
# Generic class for agent in normal-form game
    def __init__(self,name,actions=None) :
        self.name = name

class Action():
# Generic class for action in normal-form game
    def __init__(self,name,actions=None) :
        self.name = name

class Game :
# Generic class for normal-form game
    def __init__(self,players,actions,payoffs) :
        self.n = len(players)
        self.players = players
        self.actions = actions
        self.payoffs = payoffs
        
        self.checkWellPosed(self)
        
    def checkWellPosed(self):
        if not self.n == len(self.actions):
            raise IndexError('Number of players does not match number of action sets')
        # TO DO: check that the payoff matrices have correct dimensions
        #for player in self.players:
            

class GameSimple(Game) :
# This class does not use the Player or Action classes, rather referring to all by numeric index
    def __init__(self,players,actions,payoffs) :
    # players: int n
    # actions: n-D list of |A_i|
    # payoffs: high-dimensional array:
    #   dim i corresponds to player i's action,
    #   dim n tells which player's payoff we're talking about 
    
        self.n = players
        self.players = np.array(range(players))
        self.actions = [None]*self.n
        for player in self.actions :
            self.actions[player] = np.array(range(actions[player]))
        self.payoffs = payoffs
        self.checkWellPosed(self)

class GameVerbose(Game):
# Generic class for normal-form game

    def __init__(self,players,actions,payoffs) :
    # players: length-n list of players or simply n
    # actions: length-n list of lists of actions, or simply list of |A_i|
    # payoffs: 2^n dimensional array?
        
        try : # check if players arg is list or int
            self.n = len(players) # if we get a TypeError, it is an int
            self.players = players
        except TypeError: # if players argument is n
            self.n = players
            self.players = []
            for player in range(players):
                self.players.append(Player(player))
                
        # check if actions arg is the proper length
        checkWellPosed(self)
        
        try : # check if actions arg is list or int
            len(actions[0]) # checking if actions is list of lists
            self.actions = actions
        except TypeError :
            self.actions = [None]*self.n # this is the case that actions is list of numbers
            for player in range(self.n) :
                self.actions[player] = []
                for action in range(actions[player]) :
                    self.actions[player].append(Action(action))
                    
        self.payoffs = payoffs