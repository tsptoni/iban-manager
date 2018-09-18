# -*- coding: utf-8 -*-

import numpy as np
import math

def normalize(vector, scale=1):
    arr = np.array(vector)

    sumarr = sum(arr)
    if sumarr > 0:
        arr1 = arr / sumarr  # Sum total to 1.0
    else:
        arr1 = np.array([1/len(vector)]*len(vector))

    vector = arr1.tolist()
    vector = [v * scale for v in vector]

    return vector

def inner_product(i_vector, j_vector):
    pixi = 0
    pixj = 0
    pjxj = 0
    for idx, i in enumerate(i_vector):
        pixi += i * i
        pixj += i * j_vector[idx]
        pjxj += j_vector[idx] * j_vector[idx]

    pixjn = pixj / (math.sqrt(pixi) * math.sqrt(pjxj))

    return pixjn
