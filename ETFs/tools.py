# Copyright 2023-2023 Juan Sebastian Rojas Rodriguez
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np
import pandas as pd
from datetime import timedelta, date
import os


def currentRow(df):
    """
    Choice the last row the present. Besides Takes the max and min values
    of this row.
    Parameters
    ----------
    df: pandas DataFrame
        Dataframea containing returns data.

    Returns
    -------
    last_row: pandas Series
        Last returns.
    val_max: int
        Maximum value in last_row.
    val_min: int
        Minimum value in last_row.
    """
    # sort last row values
    last_row = df.iloc[-1].sort_values(ascending=False)
    # max and min values
    val_max = last_row .max()
    val_min = last_row .min()

    return last_row, val_max, val_min


def selection(serie, n=10, m_round=2):
    """
    if n>= len(serie) an n*2 serie lenght is return. Otherwise the same
    series is return.

    Parameters
    ----------
    serie: pandas Series
        Returns.
    n: int
        Amount of best and worst datra selected (each one).
        Default 10.
    m_round_: int
          Digits to Round.

    Returns
    -------
    selected: pandas Series
        Series containing best and worst returns.
    """

    if len(serie) >= n:         # how many values to select
        best = serie.iloc[:n]
        worst = serie.iloc[-n:]
        selected = pd.concat([best, worst], axis=0)
        selected = (selected * 100).round(m_round)       # porcentual change
    else:
        selected = serie
        selected = (selected * 100).round(m_round)       # porcentual change

    return selected


def dates_list(years=0, months=0, days=0):
    """
    Generates a list of dates.
    """
    # 365 days per year
    years_to_days = years * 365
    # 30 days per month
    months_to_days = months * 30

    days = days + years_to_days + months_to_days

    # boundary dates
    current_date = date.today()
    start_date = current_date - timedelta(days=days)

    weeks = int(np.ceil(days * 1/7))

    return [start_date + timedelta(days=7*i) for i in range(weeks)]


def create_dir(existing_directory, new_folder):
    """
    Parameters
    ----------
    new_folder: str
        New folder's name.
    """
    # Parent directory path
    PARENT_DIR = os.getcwd()

    # Existing Directory
    directory = f"{existing_directory}/{new_folder}"

    # Path
    path = os.path.join(PARENT_DIR, directory)

    # Create directory
    try:
        os.mkdir(path)
        return path
    except OSError:
        return path
