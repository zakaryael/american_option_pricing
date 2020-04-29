#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 01:55:15 2020

@author: zakarya_el_khiyati
"""

import project_option_pricing

market = Market(0, 0.2, 1)
asset = Asset(market, 100, m = 100)
option = TVR(asset, 90, is_put = False)
tt, S = option.asset.simulate(10)
#option.payoff(S[:, 102])
option.n = 100000

print(option.price())