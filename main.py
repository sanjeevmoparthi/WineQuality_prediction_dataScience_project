import os 
os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/Sanjeev_Moparthi/WineQuality_prediction_dataScience_project.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="Sanjeev_Moparthi"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "333be33f47e4aaaa15c23950a1655b9c3000fbbe"

import mlflow
mlflow.set_tracking_uri(os.environ["MLFLOW_TRACKING_URI"])


from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline
from src.datascience.pipeline.model_evaluation_pipeline import ModelEvaluationTrainingPipeline


STAGE_NAME = "Data Ingestion stage"


try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingestion= DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx======x")
    
    
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "MOdel validaiton stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataValidationTrainingPipeline()
    data_ingestion.initiate_data_validation()
        
        
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx======x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataTransformationTrainingPipeline()
    data_ingestion.initiate_data_transformation()
        
        
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx======x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model Trainer stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = ModelTrainerTrainingPipeline()
    data_ingestion.initiate_model_training()
        
        
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx======x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model evaluation Stage"


try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingestion= ModelEvaluationTrainingPipeline()
    data_ingestion.initiate_model_evaluation()
        
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e
     

