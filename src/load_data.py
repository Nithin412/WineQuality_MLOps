import os
from get_data import get_data,read_params
import argparse

#getting the root directory
# root_dir = os.path.normpath(os.getcwd() + os.sep + os.pardir)

def load_save(config_path):
    config = read_params(config_path)
    df = get_data(config_path)
    new_columns = [column.replace(" ", "_" ) for column in df.columns]
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    df.to_csv( raw_data_path.replace("/", "\\"),index = False, header = new_columns)

     
if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default ="params.yaml" )
    parsed_args = args.parse_args()
    load_save(config_path = parsed_args.config)