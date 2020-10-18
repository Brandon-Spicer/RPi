import numpy as np
from typing import Set, List
from nptyping import Int64, NDArray

moore = [(-1, -1), (-1, 0), (-1, 1),\
            (0, -1), (0, 1),\
            (1, -1), (1, 0), (1, 1)]


def evolve(X: NDArray, K: List, S: List, B: List) -> NDArray:
    """Return the next state of a cellular automaton."""
    adjacent = np.zeros(X.shape)
    for i, j in K:
        adjacent += np.roll(X, [i, j], [0, 1])
        
    next_state = np.where(X, np.isin(adjacent, S), np.isin(adjacent, B))
    return next_state + 0
            

def golgen(state: NDArray) -> NDArray:
    """Return a Game of Life cellular automaton generator."""
    K, S, B = moore, [2, 3], [3]
    
    while True:
        state = evolve(state, moore, S, B)
        yield state
