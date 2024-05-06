# IMPORTS

from numba import njit
import numpy as np
import glm
import math


# WINDOW RESOLUTION

WIN_RES = glm.vec2(1600, 900)


# COLOURS

BG_COLOR = (0.1, 0.1, 0.1, 1.0)