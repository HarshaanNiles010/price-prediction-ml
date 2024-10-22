import os
import sys
from datetime import datetime
import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
#from src.components.data_transformation import DataTransformation
#from src.components.data_transformation import DataTransformationConfig
#from src.components.model_trainer import ModelTrainerConfig
#from src.components.model_trainer import ModelTrainer

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = "Error ccured in python script name: [{0}] line number: [{1}] error message: [{2}]".format(
        file_name, line_number,str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
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
            df = pd.read_csv("Data/gold_price_dataset.csv")
            logging.info("read the data into a dataframe")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            logging.info("Train test split intiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Split completed")
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)

if __name__ =='__main__':
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()


