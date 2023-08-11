from PrivacyPreservingHumanPoseEstimationFromWiFi.constants import *
from PrivacyPreservingHumanPoseEstimationFromWiFi.utils.common import read_yaml, create_directories
from PrivacyPreservingHumanPoseEstimationFromWiFi.entity import DataTransformationConfig

class ConfigurationManager:
    def __init__(self, config_filepath = CONFIG_FILE_PATH, params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path,
            tokenizer_path = config.tokenizer_path,
        )
        return data_transformation_config