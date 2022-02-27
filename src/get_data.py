import os
import pandas as pd
import argparse
import yaml


#getting the root directory
root_dir = os.path.normpath(os.getcwd() + os.sep + os.pardir)

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def get_data_paramsfile(config_path):
    data = read_params(config_path)
    data_path = data["data_source"]["s3_source"]
    df = pd.read_csv(os.path.join( root_dir ,data_path))
    return df

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default =os.path.join(root_dir,"params.yaml") )
    parsed_args = args.parse_args()
    get_data_paramsfile(config_path = parsed_args.config)

    
    
    