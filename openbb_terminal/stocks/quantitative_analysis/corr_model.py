"""Corr model"""
__docformat__ = "numpy"

from typing import Optional, Tuple

import pandas as pd

from openbb_terminal.stocks import stocks_helper

def corr_model(symbol1, ref_symbol, corrperiod,  nperiods=1, start_date='2020-01-01', end_date=None, method='pearson') -> (pd.Series, str, str):
    """
    Calculate rolling correlation between nperiod returns of a given security.

    Parameters
    ----------
    symbol1: str
        Ticker you want to run the command on.
    ref_symbol: str
        Comparison ticker, defaults to spy in OPENBB terminal. 
    corrperiod: int
        The number of periods to run the rolling correlation window
    nperiod: int
        X Period returns to measure. 
    start_date: str
        date to start calculation
    end_date: str
        date to end calculation
    method: str
        pandas method to run the calculation, valid is {‘pearson’, ‘kendall’, ‘spearman’} or callable. Spearman correlation = 1.00 where both series always move in the same direction. Pearson accounts for effect size. 
    ref_data: pd.DataFrame
        The reference ticker symbols price data

    Returns
    -------
    tuple[pd.Series, str, str]
        Returns rolling correlation of given period as a series, and the tickers of each symbool
    """
    sym1 = stocks_helper.load(symbol1, start_date, end_date=end_date)
    sym2 = stocks_helper.load(ref_symbol, start_date, end_date=end_date)
    sym1[symbol1] = sym1['Close']
    sym2[ref_symbol] = sym2['Close']
    #for the correct field names

    chg1 = sym1[symbol1].pct_change(nperiods)
    chg2 = sym2[ref_symbol].pct_change(nperiods)

    return chg1.rolling(corrperiod).corr(chg2, method=method), symbol1, ref_symbol