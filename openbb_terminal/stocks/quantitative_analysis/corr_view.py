"""Corr view"""
__docformat__ = "numpy"

import logging
import os
from typing import Optional, Union

import pandas as pd

from openbb_terminal import OpenBBFigure
from openbb_terminal.decorators import log_start_end
from openbb_terminal.helper_funcs import export_data
from openbb_terminal.rich_config import console
from openbb_terminal.stocks.quantitative_analysis.corr_model import corr_model

@log_start_end(log=logger)
def call_corr(self, other_args: List[str]):
    """Process corr command"""
    parser = argparse.ArgumentParser(
        add_help=False,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        prog="corr",
        description="""
            Determine the rolling correlation between two stocks over a specified period.
        """,
    )
    parser.add_argument(
        "-s1",
        "--symbol1",
        type=str,
        dest="symbol1",
        required=True,
        help="The first stock symbol (e.g., AAPL)"
    )
    parser.add_argument(
        "-s2",
        "--ref_symbol",
        type=str,
        dest="ref_symbol",
        required=True,
        help="The reference stock symbol (e.g., MSFT) to compare with the first symbol."
    )
    parser.add_argument(
        "-cp",
        "--corrperiod",
        type=int,
        dest="corrperiod",
        default=60,
        help="The number of trading days over which to calculate the correlation."
    )
    parser.add_argument(
        "-np",
        "--nperiods",
        type=int,
        dest="nperiods",
        default=1,
        help="Number of periods to display rolling correlation."
    )
    parser.add_argument(
        "--start",
        type=str,
        dest="start_date",
        default='2020-01-01',
        help="Start date of the data in format (YYYY-MM-DD)."
    )
    parser.add_argument(
        "--end",
        type=str,
        dest="end_date",
        default=None,
        help="End date of the data in format (YYYY-MM-DD). If not provided, the current date is used."
    )
    parser.add_argument(
        "-m",
        "--method",
        dest="method",
        type=str,
        default="pearson",
        help="Method of correlation (default is 'pearson'). Options: 'pearson', 'kendall', 'spearman'."
    )
    parser.add_argument(
        "--external_axes",
        action="store_true",
        dest="external_axes",
        help="Flag to allow the use of external axes."
    )
    parser.add_argument(
        "--export",
        type=str,
        dest="export",
        default="",
        help="Path to export the data via CSV or XLSX. Leave empty to not export."
    )
    parser.add_argument(
        "--sheet_name",
        type=str,
        dest="sheet_name",
        help="Name of the sheet in case of exporting to an Excel file. Ignored if exporting to CSV."
    )

    ns_parser = self.parse_known_args_and_warn(parser, other_args)
    if ns_parser:
        try:
            # Assuming corr_view is a function that processes the correlation view.
            # The arguments match the parameters of the corr_view function.
            corr_view(
                symbol1=ns_parser.symbol1,
                ref_symbol=ns_parser.ref_symbol,
                corrperiod=ns_parser.corrperiod,
                nperiods=ns_parser.nperiods,
                start_date=ns_parser.start_date,
                end_date=ns_parser.end_date,
                method=ns_parser.method,
                external_axes=ns_parser.external_axes,
                export=ns_parser.export,
                sheet_name=ns_parser.sheet_name
            )
        except Exception as e:
            # Handle exceptions as per the application's general exception handling strategy
            print(f"An error occurred: {str(e)}")