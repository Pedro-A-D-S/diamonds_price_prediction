import pandas as pd
import seaborn as sns

def plot_quantity(data, col):
    ax = sns.set(rc = {'figure.figsize': (10, 6)})
    order = data[col].value_counts().index
    ax = sns.countplot(x = col, data = data, order = order)
    ax.set_title('Quantity of diamonds by {}'.format(col), fontsize = 16)
    ax.set_xlabel(f'{col}', fontsize = 14)
    ax.set_ylabel('Quantity', fontsize = 14)
    ax = ax
    return ax

def mean_price_by_cathegory(data, col):
    mean_price_by_cathegory = data.groupby([col]).mean().price.round(2).sort_values(ascending = False).reset_index()
    mean_price_by_cathegory = pd.DataFrame(mean_price_by_cathegory)
    mean_price_by_cathegory.rename(columns = {'price':'mean price'}, inplace = True)
    mean_price_by_cathegory
    
    return mean_price_by_cathegory

def median_price_by_cathegory(data, col):
    median_price_by_cathegory = data.groupby([col]).median().price.round(2).sort_values(ascending = False).reset_index()
    median_price_by_cathegory = pd.DataFrame(median_price_by_cathegory)
    median_price_by_cathegory.rename(columns = {'price':'median price'}, inplace = True)
    median_price_by_cathegory
    
    return median_price_by_cathegory

def std_price_by_cathegory(data, col):
    std_price_by_clarity = data.groupby([col]).std().price.round(2).sort_values(ascending = False).reset_index()
    std_price_by_clarity = pd.DataFrame(std_price_by_clarity)
    std_price_by_clarity.rename(columns = {'price':'std of price'}, inplace = True)
    std_price_by_clarity

    return std_price_by_clarity