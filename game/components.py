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
    def __init__(self,players,actions,pmat) :
        self.n = len(players)
        self.players = players
        self.actions = actions
        self.pmat = pmat
        
        self.checkWellPosed()
        
    def checkWellPosed(self):
        return
        # TO DO: check that the payoff matrices have correct dimensions
        #for player in self.players:
            
    def checkActions(self) :
        if not self.n == len(self.actions):
            raise IndexError('Number of players does not match number of action sets')
            
    def checkpmat(self) :
        # checks if payoff matrices are well-define dimensionally (does not check array contents)
        if not self.n + 1 == self.pmat.ndim :
            raise IndexError('payoff matrix has wrong number of dimensions')
        for player in self.players :
            if not len(self.actions[player]) == np.shape(self.pmat)[player] :
                errMsg = 'Player %d (0-indexed) has the wrong number of actions' % player
                raise IndexError(errMsg)
        if not self.n == np.shape(self.pmat)[self.n] :
            raise IndexError('the wrong number of players\' actions are being described')


class GameSimple(Game) :
# This class does not use the Player or Action classes, rather referring to all by numeric index
    def __init__(self,players,actions,pmat) :
    # players: int n
    # actions: n-D list of |A_i|
    # pmat: (n+1)-dimensional array:
    #   dim i corresponds to player i's action; np.shape(pmat[i])=|A_i|
    #   dim n tells which player's payoff we're talking about ; np.shape(pmat[n])=n
    
        self.n = players
        self.players = np.array(range(players))
        self.actions = [None]*len(actions)
        self.checkActions()
        for player in self.players :
            self.actions[player] = np.array(range(actions[player]))
        self.pmat = pmat
        self.checkpmat()

class GameVerbose(Game):
# Generic class for normal-form game

    def __init__(self,players,actions,pmat) :
    # players: length-n list of players or simply n
    # actions: length-n list of lists of actions, or simply list of |A_i|
    # pmat: 2^n dimensional array?
        
        try : # check if players arg is list or int
            self.n = len(players) # if we get a TypeError, it is an int
            self.players = players
        except TypeError: # if players argument is n
            self.n = players
            self.players = []
            for player in range(players):
                self.players.append(Player(player))
                
        # check if actions arg is the proper length
        self.checkWellPosed()
        
        try : # check if actions arg is list or int
            len(actions[0]) # checking if actions is list of lists
            self.actions = actions
        except TypeError :
            self.actions = [None]*self.n # this is the case that actions is list of numbers
            for player in range(self.n) :
                self.actions[player] = []
                for action in range(actions[player]) :
                    self.actions[player].append(Action(action))
                    
        self.pmat = pmat