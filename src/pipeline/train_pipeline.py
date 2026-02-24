import os
import sys
from src.exception import CustomException
from src.logger import logging

from src.components.data_ingestion import DataIngestion
from src.components.data_tranform import DataTransformation 
from src.components.model_trainer import ModelTrainer
if __name__ == "__main__":
    try:
        obj = DataIngestion()
        train_data, test_data = obj.initiate_data_ingestion()
        data_transformation = DataTransformation()
        train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)
        model_trainer = ModelTrainer()
        model_trainer.initiate_model_trainer(train_arr, test_arr)
    except Exception as e:
        raise CustomException(e, sys)
    
# import sys
# from src.exception import CustomException
# from src.logger import logging

# # Import components
# from src.components.data_ingestion import DataIngestion
# from src.components.data_tranform import DataTransformation
# from src.components.model_trainer import ModelTrainer


# class TrainPipeline:
#     def __init__(self):
#         pass

#     def run_pipeline(self):
#         try:
#             logging.info("Starting Training Pipeline")

#             # STEP 1 → Data Ingestion
#             data_ingestion = DataIngestion()
#             train_data, test_data = data_ingestion.initiate_data_ingestion()
#             logging.info("Data Ingestion Completed")

#             # STEP 2 → Data Transformation
#             data_transformation = DataTransformation()
#             train_arr, test_arr, _ = data_transformation.initiate_data_transformation(
#                 train_data,
#                 test_data
#             )
#             logging.info("Data Transformation Completed")


#             # STEP 3 → Model Training
#             model_trainer = ModelTrainer()
#             model_trainer.initiate_model_trainer(train_arr, test_arr)
#             logging.info("Model Training Completed")
#             logging.info("Training Pipeline Finished Successfully")

#         except Exception as e:
#             raise CustomException(e, sys)

# if __name__=="__main__":
#     obj = TrainPipeline()
#     obj.run_pipeline()