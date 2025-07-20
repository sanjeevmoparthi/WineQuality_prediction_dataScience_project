import os
import yaml
from src.datascience import logger
import json
import joblib 
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path 
from typing import Any
from box.exceptions import BoxValueError

# @ensure_annotations
# def read_yaml(path_to_yaml: Path) -> ConfigBox:
#     '''reads yaml file and returns
#     Args:
#     path_to_yaml (str): path like input

#     Raises:
#         ValueError: if yaml file is empty
#         e: empty file 
#     Returns:
#         ConfigBox:ConfigBox type
#     '''

#     try:
#         with open(path_to_yaml) as yaml_file:
#             content = yaml.safe_load(yaml_file)
#             logger.info(f"yaml file: {path_to_yaml} loaded successfully")
#             return ConfigBox(content)
        
#     except BoxValueError:
#         raise ValueError("yaml file is empty")
#     except Exception as e:
#         raise e


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox (dict with attribute-style access).

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the YAML file is empty.
        Exception: If any other unexpected error occurs.

    Returns:
        ConfigBox: Contents of the YAML file.
    """
    if not path_to_yaml.exists():
        raise FileNotFoundError(f"YAML file not found at: {path_to_yaml}")

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise ValueError(f"YAML file is empty: {path_to_yaml}")
            logger.info(f"YAML file loaded successfully: {path_to_yaml}")
            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("YAML content is not a valid mapping")
    except Exception as e:
        raise e

    

@ensure_annotations
def create_directories(path_to_directories: list,verbose = True):
    """create list of directories
    Args:
    path_to_directories(list): list of path of directories
    ignore_log(bool,optional): ignore if multiple dirs is to be created. """


    for path in path_to_directories:
        os.makedirs(path,exist_ok = True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path,data: dict):
    """save json data
    Args: 
        path(Path): path to json file 
        data(dict): data to be saved in json file """

    with open(path,"w") as f:
        json.dump(data,f,indent = 4)

    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json file data
    Args:
    path(Path): path to json file 
    Returns:
    Configbox: data as class attributes instead of dict"""

    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded successfully from :{path}")
    return ConfigBox(content)
    






