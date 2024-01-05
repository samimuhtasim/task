def calculate_incidence_rate(data, count_column, population_column):
    """
    Calculate the incidence rate of a health condition.

    Parameters:
    - data: DataFrame containing health data.
    - count_column: String, the name of the column containing the case counts.
    - population_column: String, the name of the column containing population data.

    Returns:
    - DataFrame with an additional column 'IncidenceRate'.
    """
    data['IncidenceRate'] = (data[count_column] / data[population_column]) * 100000
    return data