import datetime
from sklearn.model_selection import train_test_split
import numpy as np

def str_to_datetime(s):
    try:
        split = s.split('-')
        day, month, year = int(split[0]), int(split[1]), int(split[2])
        return datetime.datetime(day=day, month=month, year=year)
    except ValueError:
        print(f"Invalid date string: {s}")
        return None
    
def split_dataset(X_data, y_data, dates):
    # Split data into train, val and test. Note that 'shuffle=False' due to time-series data.
    X_train, X_test, y_train, y_test, train_dates, test_dates = train_test_split(X_data, y_data, dates, test_size=0.2, shuffle=False)
    X_train, X_val, y_train, y_val, train_dates, val_dates = train_test_split(X_train, y_train, train_dates, test_size=0.2, shuffle=False)

    # Convert from lists to Numpy arrays for reshaping purpose
    X_train = np.array(X_train)
    X_val = np.array(X_val)
    X_test = np.array(X_test)
    y_train = np.array(y_train)
    y_val = np.array(y_val)
    y_test = np.array(y_test)

    return X_train, y_train, X_val, y_val, X_test, y_test, train_dates, val_dates, test_dates

def normalize_data(X, y):
    # MinMax normalize the training data: x=(x-min(x)/(max(x)-min(x))
    X_norm = X.copy()
    y_norm = y.copy()
    for i in range(0, len(X)):
        min_feature = np.min(X[i])
        max_feature = np.max(X[i])
        X_norm[i] = (X[i] - min_feature) / (max_feature - min_feature)
        y_norm[i] = (y[i] - min_feature) / (max_feature - min_feature)
    return X_norm, y_norm
def denorm_data(y_pred_norm):
    y_pred_denorm = y_pred_norm
    for i in range(0, len(y_pred_denorm)): # denorm_x = norm_x * (max(x) - min(x)) + min(x)
        min_feature = np.min(X_test[i])
        max_feature = np.max(X_test[i])
        y_pred_denorm[i] = y_pred_norm[i] * (max_feature - min_feature) + min_feature
    return y_pred_denorm