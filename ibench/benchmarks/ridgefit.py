# Copyright (C) 2018 Intel Corporation
#
# SPDX-License-Identifier: MIT

import numpy as np
import sklearn
import multiprocessing
from numpy.random import rand
from sklearn import linear_model

from .bench import Bench

if sklearn.__version__ == '0.18.2':
    sklearn.utils.validation._assert_all_finite = lambda X: None 

class Ridgefit(Bench):
    """
    Benchmark for Ridge Regression Prediction from Scikit-learn
    Attempts to utilize parallelism for larger datasets
    """
    sizes = {'large': 1000000, 'small': 800000, 'tiny': 100000, 'test': 1000}

    def _ops(self, n):
        return 2E-9 * n*n*n

    def _make_args(self, n):
        p = int(np.log(n)+100)
        self._X = rand(n,p)
        self._y = rand(n)
        self._regr = linear_model.Ridge()
        self._regr.fit(self._X,self._y)

    def _compute(self):
        self._regr.predict(self._X)
