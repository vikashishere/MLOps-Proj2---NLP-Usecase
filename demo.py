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

from hate.logger import logging
from hate.exception import CustomException
import sys
from hate.configuration.gcloud_syncer import GCloudSync

obj = GCloudSync()
obj.sync_folder_from_gcloud("mlops-proj2-hatespeech", "dataset.zip", "download/dataset.zip")