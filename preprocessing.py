def handle_missing_values(data, method='drop'):
    """
    Handle missing values in a DataFrame.

    Parameters:
    - data: DataFrame with missing values.
    - method: String, method to handle missing values ('drop' or 'fill').

    Returns:
    - DataFrame with handled missing values.
    """
    
    infected_columns = data.columns[10:21]
    data['Initial_Infected'] = data[infected_columns].sum(
        axis=1)
    
    data['Population'] = data['SPEC_PROCESSED_NB']


    if method == 'drop':
        return data.dropna()
    elif method == 'fill':
        return data.fillna(method='ffill')
    else:
        raise ValueError('Invalid method for handling missing values')
    
    import pandas as pd


