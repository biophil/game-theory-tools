# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 15:35:22 2016

@author: Philip
"""
import numpy as np

# small number for zero-checking floats:
myEps = 1e-10

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
            
    def checkActionProfile(self,actionProfile) :
        for player in range(len(actionProfile)) :
            stratWeights = np.array(actionProfile[player])
            # first check that the strategy has the correct length:
            if not len(self.actions[player]) == len(stratWeights) :
                raise IndexError('player %d (0-indexed) does not have correct number of action weights specified' % player)
            # then check that every action weight is nonnegative:
            for action in range(len(stratWeights)) :
                if not stratWeights[action] >= -myEps :
                    raise TypeError('action %d for player %d has a negative weight' %(action, player)) #TypeError might not be best exception
            # finally check that mixed weights add to 1 (so it's valid probabilities):
            if not np.abs(np.sum(stratWeights)-1) <= myEps :
                raise TypeError('action weights for player %d do not sum to 1' % player) # again, TypeError might not be best
            
    def payoffs(self,playersArg,actionProfile) :
        # returns the payoffs experienced by playersArg given mixed strategies actionProfile
        # playersArg: list of player indices we wish to check
        # actionProfile: N-D list of 1-D arrays of mixed strategies;
        #    len(actionProfile[i]) = len(self.actions[i])
        # output: array of dimension len(playersArg) of player payoffs
        ap = np.array(actionProfile)
        self.checkActionProfile(ap)
        # first, collapse the payoff matrix using the action profile:
        pmatCollapsed = np.array(self.pmat)
        for player in self.players :
            vecShape = np.ones(len(np.shape(pmatCollapsed)))
            vecShape[0] = len(ap[player]) # vecShape ensures that strategy weights are multiplied in properly
            thisPmat = pmatCollapsed*np.reshape(ap[player],vecShape) # multiply strat weights
            pmatCollapsed = np.sum(thisPmat,0) # sum along dimension 0
        return pmatCollapsed[np.array(playersArg)]


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

