# game-theory-tools
This is intended to be a set of tools for analyzing normal-form games, particularly with an eye to simulating dynamics and learning.

## Class `Game()`
Basic class for representing a game. Initialization tools exist in the subclass `GameSimple()`.

### `Game()` attributes:

* `n` number of players
* `players` vector of player indices, essentially `range(n)`
* `actions` list of lists of player actions
* `pmat` payoff matrix. Each of dimensions `0` thru `n-1` corresponds to a player ID, dim `n` specifies which player's payoff is being described. Example: `pmat[4,5,6,0]` represents player `0`'s payoff when players `0,1,2` are playing actions `4,5,6` respectively. Note that `print(game.pmat)` is fairly unintelligible for games larger than 2x2.

### `Game()` methods:

* `payoffs(players,actionProfile)` returns the payoffs experienced by `players` under mixed strategy action profile `actionProfile`. `players` is a list of player indices, and `actionProfile` is a complete list of all players' mixed strategies, represented as a list-of-lists. This method outputs an array of floats of length `len(players)`.
* `payoffVec(player,actionProfileReduced)` returns the payoffs experienced by `player` when all others are playing mixed strategies given by `actionProfileReduced` (which is of dimension `n-1`). The output is an array of floats of length `len(self.actions[player])`, i.e., it gives the payoff associated with each of `player`'s possible actions.


## Class `GameSimple(Game)`
Only difference from `Game` is the `__init()` method.
### `GameSimple(Game)` methods:

* `__init__(players,actions,pmat)` takes integer `players`, length-n list of action sets `actions`, and fully-specified payoff matrices `pmat` (format described above).
