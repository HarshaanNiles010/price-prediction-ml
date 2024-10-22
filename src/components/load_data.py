import os
import sys
from src.exception import CustomException
from logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
#from src.components.data_transformation import DataTransformation
#from src.components.data_transformation import DataTransformationConfig
#from src.components.model_trainer import ModelTrainerConfig
#from src.components.model_trainer import ModelTrainer


class DataIngestionConfig():
    train_data_path: str = os.path.join('artifacts','train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts','dataset.csv')

class DataIngestion():
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Entered data ingestion")
        try:
            df = pd.read_csv("../Data/gold_price_dataset.csv")
            logging.info("read the data into a dataframe")
            os.mkdirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            logging.info("Train test split intiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Split completed")
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_cnofig.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)

if __name__ =='__main__':
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()


