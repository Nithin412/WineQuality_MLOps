"""Agenda of this file
   load the dataset from data/preprocessed directory
   train the algorithm 
   save the metrics and the parameters"""

import os
import pandas as pd
import numpy as np
import warnings
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.linear_model import ElasticNet
import joblib
import json
from get_data import read_params
from sklearn.model_selection import train_test_split
import argparse
from urllib.parse import urlparse


def train_and_evaluate(config_path):
    config = read_params(config_path)
    train_data_path = config["split_data"]["train_path"]
    test_data_path = config["split_data"]["test_path"]
    random_state = config["base"]["random_state"]
    model_dir = config["model_dir"]

    alpha = config["estimators"]["ElasticNet"]["params"]["alpha"]
    l1_ratio = config["estimators"]["ElasticNet"]["params"]["l1_ratio"]

    target = list(config["base"]["target_col"])

    train = pd.read_csv(train_data_path, sep=",")
    test = pd.read_csv(test_data_path, sep=",")

    train_x = train.drop([target], axis=1)
    test_x = test.drop([target], axis=1)

    train_y = train[target]
    test_y = test[target]


if __name__ == "__main__":
    pass
