import pandas as pd

def outlier_removal(df: pd.DataFrame) -> pd.DataFrame:
    """
    Removes outliers from the specified columns of the input DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: DataFrame with outliers removed.

    """
    # column names
    columns = ['x', 'y', 'z', 'table', 'depth']

    for column in columns:
        # defining series of variable
        x = df[column]

        # quantiles and interval interquantile
        Q1 = x.quantile(.45)
        Q3 = x.quantile(.75)
        IIQ = Q3 - Q1

        # lower and upper limits
        lower_limit = Q1 - 1.5 * IIQ
        upper_limit = Q3 + 1.5 * IIQ

        # filtering by limits
        selection = (x >= lower_limit) & (x <= upper_limit)
        df = df[selection]
    
    return df

def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Removes duplicate rows from the input DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: DataFrame with duplicate rows removed.

    """
    # dropping duplicates
    df = df.drop_duplicates()
    return df
