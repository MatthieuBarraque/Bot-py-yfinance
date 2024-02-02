#!/usr/bin/env python

"""
test.py:
    This file contains the test function
"""

import yfinance as yf

msft = yf.Ticker("MSFT")

# get stock info
print(msft.info)
