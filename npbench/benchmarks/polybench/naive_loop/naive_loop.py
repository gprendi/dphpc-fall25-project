# Copyright 2021 ETH Zurich and the NPBench authors. All rights reserved.

import numpy as np


def initialize(M, datatype=np.float64):
    data = np.zeros((M, ), dtype=datatype)
    return data
