#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 12:36:17 2020

@author: zakarya_el_khiyati
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

class Market(object):
    def __init__(self, rate, volatility, T):
        self.rate = rate
        self.volatility = volatility
        self.T = T

class Asset(object):
    """risky asset"""
    def __init__(self, market, initialPrice, m = 1):
        self.market = market
        self.initialPrice = initialPrice
        self.m = m #time steps
    def simulate(self, n):
        """simulates n independent trajectories of an asset following the Black Scholes model"""
        """ each line is an independent trajectory"""
        m = self.m
        T = self.market.T
        tt = np.linspace(0, T, m + 1)
        S = np.zeros((n, m + 1))
        for i in range(n):
            z = np.random.normal(0, np.sqrt(1 / (m)), m + 1)
            z[0] = 0
            w = np.cumsum(z)
            S[i] = self.initialPrice * np.exp((market.rate - market.volatility ** 2 / 2) * tt + market.volatility * w)
        if (m == 1):
            return S[:, m]
        else:
            return tt, S
    def trajectory(self):
        """plots a trajectory of the asset price"""
        traj = self.simulate(1)
        xaxis = traj[0]
        yaxis = traj[1][0]
        plt.plot(xaxis, yaxis, 'r')
        plt.show()

    def bin_tree(self, N):
        """computes the matrix of prices in the CRR model of N periods"""
        pass

class Option(object):
    def __init__(self, asset, strike, is_put = True, is_american = True):
        self.market = market
        self.asset = asset
        self.strike = strike
        self.is_put = is_put
        self.is_american = is_american
        self.m = asset.m
    def payoff(self, x):
        if self.is_put:
            return np.maximum(0, self.strike - x)
        else:
            return np.maximum(0, x - self.strike)
    def price(self):
        pass

class TVR(Option):
    """pricing an american option using the Tsitsikliss Van Roy method"""
    n = 10000
    def regression(self, x, y):
        x2 = self.payoff(x)
        X = np.column_stack((x, x2))
        #model = make_pipeline(PolynomialFeatures(4), LinearRegression()) #to use this you need to import more lib
        model = linear_model.LinearRegression()
        model.fit(X, y)
        return model.predict(X)

    def recursion(self, S):
        m = self.m
        n = self.n
        V = np.zeros((n, m + 1))
        V[:, self.m] = self.payoff(S[:, self.m])
        for i in range(m - 1, 0, -1):
            V[:, i] = np.maximum(self.payoff(S[:, i + 1]), self.regression(S[:, i], V[: ,i + 1]))
        return V

    def price(self):
        S = self.asset.simulate(self.n)[1]
        V = self.recursion(S)
        return np.mean(V[:, 1])

class LongShwartz(TVR):
    """docstring for LongShwartz."""
    pass
