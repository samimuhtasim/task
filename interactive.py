import plotly.express as px

def interactive_scatter(data, x_column, y_column, title='Interactive Scatter Plot'):
    fig = px.scatter(data, x=x_column, y=y_column, title=title)
    fig.show()
    return fig