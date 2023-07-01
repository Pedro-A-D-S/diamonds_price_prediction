import pandas as pd
import seaborn as sns
from typing import Union
import matplotlib.pyplot as plt


def plot_quantity(data: pd.DataFrame, col: str) -> plt.Axes:
    """
    Plots the quantity of items by a specific category in a bar chart.

    Args:
        data (pd.DataFrame): The input DataFrame containing the data.
        col (str): The column name representing the category.

    Returns:
        plt.Axes: The plot object representing the bar chart.
    """
    ax = sns.set(rc={'figure.figsize': (10, 6)})
    order = data[col].value_counts().index
    ax = sns.countplot(x=col, data=data, order=order)
    ax.set_title(f'Quantity of items by {col}', fontsize=16)
    ax.set_xlabel(col, fontsize=14)
    ax.set_ylabel('Quantity', fontsize=14)
    return ax


def calculate_price_statistics(data: pd.DataFrame, col: str, statistic: str) -> pd.DataFrame:
    """
    Calculates the specified statistic (mean, median, or standard deviation) of prices
    grouped by a specific category.

    Args:
        data (pd.DataFrame): The input DataFrame containing the data.
        col (str): The column name representing the category.
        statistic (str): The statistic to calculate ('mean', 'median', or 'std').

    Returns:
        pd.DataFrame: The DataFrame with the calculated statistic for each category.
    """
    if statistic == 'mean':
        result = data.groupby([col])['price'].mean()
    elif statistic == 'median':
        result = data.groupby([col])['price'].median()
    elif statistic == 'std':
        result = data.groupby([col])['price'].std()
    else:
        raise ValueError("Invalid statistic. Must be one of: 'mean', 'median', 'std'.")

    result = result.round(2).sort_values(ascending=False).reset_index()
    result.rename(columns={'price': f'{statistic} price'}, inplace=True)
    return result


def mean_price_by_category(data: pd.DataFrame, col: str) -> pd.DataFrame:
    """
    Calculates the mean price of items grouped by a specific category.

    Args:
        data (pd.DataFrame): The input DataFrame containing the data.
        col (str): The column name representing the category.

    Returns:
        pd.DataFrame: The DataFrame with the mean price for each category.
    """
    return calculate_price_statistics(data, col, 'mean')


def median_price_by_category(data: pd.DataFrame, col: str) -> pd.DataFrame:
    """
    Calculates the median price of items grouped by a specific category.

    Args:
        data (pd.DataFrame): The input DataFrame containing the data.
        col (str): The column name representing the category.

    Returns:
        pd.DataFrame: The DataFrame with the median price for each category.
    """
    return calculate_price_statistics(data, col, 'median')


def std_price_by_category(data: pd.DataFrame, col: str) -> pd.DataFrame:
    """
    Calculates the standard deviation of prices of items grouped by a specific category.

    Args:
        data (pd.DataFrame): The input DataFrame containing the data.
        col (str): The column name representing the category.

    Returns:
        pd.DataFrame: The DataFrame with the standard deviation of prices for each category.
    """
    return calculate_price_statistics(data, col, 'std')
