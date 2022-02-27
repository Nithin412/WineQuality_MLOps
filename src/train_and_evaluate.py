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
