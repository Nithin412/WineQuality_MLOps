import os
import pandas as pd
from sklearn.model_selection import train_test_split
import argparse
from get_data import read_params


def split_and_save_data(config_path):
    config = read_params(config_path)
    train_data_path = config["split_data"]["train_path"]
    test_data_path = config["split_data"]["test_path"]
    test_size = config["split_data"]["test_size"]
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    random_state = config["base"]["random_state"]
    
    df = pd.read_csv(raw_data_path, sep = ",")
    train, test = train_test_split(df, test_size = test_size, random_state= random_state)
    
    #saving the train and test dataframe to the respective processed folder
    train.to_csv(train_data_path, index = False, sep = ',')
    test.to_csv(test_data_path, index = False, sep = ',')


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default ="params.yaml" )
    parsed_args = args.parse_args()
    split_and_save_data(config_path = parsed_args.config)