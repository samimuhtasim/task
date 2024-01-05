import pandas as pd

def load_data(file_path, file_type='csv'):
    """
    Load data from a specified file.

    Parameters:
    - file_path: String, the path to the data file.
    - file_type: String, the type of the file ('csv', 'excel', 'json', etc.).

    Returns:
    - DataFrame containing the loaded data.
    """
    if file_type == 'csv':
        return pd.read_csv(file_path)
    elif file_type == 'excel':
        return pd.read_excel(file_path)
    elif file_type == 'json':
        return pd.read_json(file_path)
    else:
        raise ValueError('Unsupported file type')

def save_data(data, file_path, file_type='csv'):
    """
    Save a DataFrame to a specified file.

    Parameters:
    - data: DataFrame to be saved.
    - file_path: String, the path to save the file.
    - file_type: String, the type of the file ('csv', 'excel', 'json', etc.).
    """
    if file_type == 'csv':
        data.to_csv(file_path, index=False)
    elif file_type == 'excel':
        data.to_excel(file_path, index=False)
    elif file_type == 'json':
        data.to_json(file_path, orient='records', lines=True)
    else:
        raise ValueError('Unsupported file type')