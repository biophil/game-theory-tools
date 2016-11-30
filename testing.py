# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 15:33:51 2016

@author: Philip
"""

import numpy as np
import game.components as gm

def max_evaluator(pmat) :
    # assumes game has 3 players
    playerpayoffs = pmat[0]
    for i,layer in enumerate(playerpayoffs) :
        for j,row in enumerate(layer) :
            thispayoff = max(row)
            playerpayoffs[i][j] = np.array([thispayoff,thispayoff])

def playerIndex(player,n) :
    # inputs the real player index (0-indexed), outputs the internal index
    # i.e.: 2->0, 3->1, 1->(n-1), 0->(n-2)
    assert player >= 0 and player <n
    return (player+1)%n

# code for the Identical-Interest pathology
EP = 0.1
players = list(range(0,3))
actions = [[0,1,2],[0,1],[0,1]]
pmat = np.zeros(help.getPayoffMatrixShape(players,actions))
basepayoffs = pmat[0].copy()
basepayoffs[0] = np.array([[1,1-2*ep],
                          [1-3*ep,1-ep],
                          [0,0]])
basepayoffs[1] = np.array([[0,0],
                          [1-3*ep,1-3*ep],
                          [1-ep,1-ep]])
for i in range(0,3) :
    pmat[i] = basepayoffs.copy()
max_evaluator(pmat)
# that's it, the payoff matrix with the max-evaluator applied

G = gm.NormalFormGame(players,actions,pmat)