#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 09:09:29 2016

@author: pnbrown
"""

# assumes that we have a game G to learn, initialized by some other script

import testing

try :
    mem
except NameError :
    mem = []
    


mem += testing.G.log_linear_learn(.005,maxIter=10000)

