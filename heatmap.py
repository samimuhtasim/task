import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

def generate_heat_map(data, country_column, count_column, thresholds=None, colors=None, title='Heat Map'):
    # Set default thresholds and colors if none provided
    if thresholds is None:
        thresholds = [1000, 10000]
    if colors is None:
        colors = ['green', 'yellow', 'red']
    
    # Load a world map for plotting
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    # Merge the data with the world map
    world = world.merge(data, how='left', left_on='name', right_on=country_column)

    # Define color categories
    cmap = ListedColormap(colors)
    world['Category'] = pd.cut(world[count_column], [-float('inf')] + thresholds + [float('inf')], labels=colors)

    # Plot the world map with the color-coded data
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    world.boundary.plot(ax=ax, linewidth=1, color='Black')
    world[world['Category'].isna()].plot(ax=ax, color='lightgrey')
    for color in colors:
        world[world['Category'] == color].plot(ax=ax, color=color)
    
    ax.set_title(title)
    plt.show()
    return fig


def generate_vaccine_based_heat_map(data, geo_data=world, location_column, vaccines_supplied_column, vaccines_required_column, title='Vaccine Based Heat Map'):
    """
    Generates a heat map that changes color based on the ratio of vaccines supplied to vaccines required.

    Parameters:
    - data: DataFrame containing the dataset.
    - geo_data: Geopandas DataFrame with geographical data for the heatmap.
    - location_column: Column name representing the location.
    - vaccines_supplied_column: Column name representing the number of vaccines supplied.
    - vaccines_required_column: Column name representing the number of vaccines required.
    - title: Title of the heat map.
    """
    # Merge the data with geographical data
    merged_data = geo_data.merge(
        data, left_on=location_column, right_on=location_column)

    # Calculate the ratio of vaccines supplied to required
    merged_data['vaccine_ratio'] = merged_data[vaccines_supplied_column] / \
        merged_data[vaccines_required_column]

    # Define the color scheme
    cmap = ListedColormap(['red', 'yellow', 'green'])
    merged_data['color'] = pd.cut(merged_data['vaccine_ratio'], bins=[
                                  0, 0.5, 1, np.inf], labels=[0, 1, 2])

    # Plot the heat map
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    merged_data.plot(column='color', cmap=cmap,
                     linewidth=0.8, ax=ax, edgecolor='0.8')
    ax.set_title(title)
    plt.show()
