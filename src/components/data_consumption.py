import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
import requests
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score,train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error,r2_score


def observe_data(path_to_data_set: str):
    data = pd.read_csv("gold_price_dataset.csv")
    print(data.head())
    
