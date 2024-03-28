# Below 2 lines of code are for the testing purpose for logging

# from hate.logger import logging
# logging.info("Welcome to the project")
# ----------------------------------------------------------------------

# Below code block is for the testing purpose for exception module
# from hate.logger import logging
# from hate.exception import CustomException
# import sys


# try:
#     a = "hello"/0
# except Exception as e:
#     raise CustomException(e, sys)
# ----------------------------------------------------------------------

# Below code block is for the testing purpose for downloading data from gcloud storage
# from hate.logger import logging
# from hate.exception import CustomException
# import sys
# from hate.configuration.gcloud_syncer import GCloudSync

# obj = GCloudSync()
# obj.sync_folder_from_gcloud("mlops-proj2-hatespeech", "dataset.zip", "download")

# ----------------------------------------------------------------------
from hate.logger import logging
from hate.exception import CustomException
import sys
from hate.configuration.gcloud_syncer import GCloudSync
from hate.components.data_ingestion import DataIngestion
from hate.entity.config_entity import DataIngestionConfig
import os
from zipfile import ZipFile
from hate.logger import logging
from hate.exception import CustomException
from hate.configuration.gcloud_syncer import GCloudSync
from hate.entity.config_entity import DataIngestionConfig
from hate.entity.artifact_entity import DataIngestionArtifacts

obj = DataIngestion(DataIngestionConfig)
obj.get_data_from_gcloud()








