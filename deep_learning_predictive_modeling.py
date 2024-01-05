import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def neural_network_predict(data, feature_columns, target_column):
    """
    Train and apply a neural network model.

    Parameters:
    - data: DataFrame containing the dataset.
    - feature_columns: List of columns to be used as features.
    - target_column: Column to be used as the target variable.

    Returns:
    - DataFrame with predictions.
    """
    # Preparing the data
    X = data[feature_columns]
    y = data[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Feature scaling
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Building the model
    model = Sequential()
    model.add(Dense(128, activation='relu', input_shape=(X_train.shape[1],)))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(1, activation='linear'))

    # Compiling the model
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Training the model
    model.fit(X_train, y_train, epochs=10, batch_size=32)

    # Making predictions
    predictions = model.predict(X_test)
    data.loc[X_test.index, 'Predictions'] = predictions.flatten()
    return data