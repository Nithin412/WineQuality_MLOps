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

# This function is used to return rmse, mae and r2 score metrics
def evaluate_metrics(predict, actual):
    rmse = (mean_squared_error(actual, predict)) ** 0.5
    mae = mean_absolute_error(actual, predict)
    r2 = r2_score(actual, predict)
    return rmse, mae, r2


def train_and_evaluate(config_path):
    config = read_params(config_path)
    train_data_path = config["split_data"]["train_path"]
    test_data_path = config["split_data"]["test_path"]
    random_state = config["base"]["random_state"]
    model_dir = config["model_dir"]

    alpha = config["estimators"]["ElasticNet"]["params"]["alpha"]
    l1_ratio = config["estimators"]["ElasticNet"]["params"]["l1_ratio"]

    target = [config["base"]["target_col"]]

    train = pd.read_csv(train_data_path, sep=",")
    test = pd.read_csv(test_data_path, sep=",")

    train_x = train.drop(target, axis=1)
    test_x = test.drop(target, axis=1)

    train_y = train[target]
    test_y = test[target]

    lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=random_state)
    lr.fit(train_x, train_y)

    pred_y = lr.predict(test_x)

    (rmse, mae, r2) = evaluate_metrics(pred_y, test_y)

    # now we want to track the parameters and the scores in to a json file
    params_path = config["reports"]["params"]
    scores_path = config["reports"]["scores"]

    with open(params_path, "w") as params_file:
        params = {"alpha": alpha, "l1_ratio": l1_ratio}
        json.dump(params, params_file)
    with open(scores_path, "w") as scores_file:
        scores = {"rmse": rmse, "mae": mae, "r2": r2}
        json.dump(scores, scores_file)
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "model.joblib")

    # saving the model.There are two ways to save a model
    # 1) is to use pickle if we want to store in the form bytes not suitable for large file
    # so we are going with joblib

    joblib.dump(lr, model_path)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    train_and_evaluate(config_path=parsed_args.config)
