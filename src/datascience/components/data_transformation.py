import os
from src.datascience import logger 
from sklearn.model_selection import train_test_split
import pandas as pd

from src.datascience.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self,config: DataTransformationConfig):
        self.config = config

        # Note you can add different data transformation such as scaler ,pca and all
        # you can perform all kinds of EDA in ML cycle here before passing the data to the model

        # I am only adding train_test_splitting cz this data is alredy cleaned up



    def train_test_splitting(self):
        data= pd.read_csv(self.config.data_path)

        # Split the data into training and test sets.(0.75,0.25) split.
        train,test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index = False)
        train.to_csv(os.path.join(self.config.root_dir,"test.csv"),index = False)

        logger.info("Splitted data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)

