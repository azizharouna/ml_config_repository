import pytest
from pathlib import Path
from unittest.mock import patch
from ml_config_repository.core.manager import UseCaseManager, DataValidator

class TestUseCaseManager:
    def setup_method(self):
        UseCaseManager._registry = {}
        
    def test_add_and_get_config(self):
        test_config = {"model": "XGBoost", "params": {"max_depth": 6}}
        UseCaseManager.add_config("test_case", test_config)
        assert UseCaseManager.get_config("test_case") == test_config
        
    def test_get_nonexistent_config(self):
        assert UseCaseManager.get_config("missing") is None
        
    def test_load_from_dir(self, tmp_path):
        config_dir = tmp_path / "configs"
        config_dir.mkdir()
        config_file = config_dir / "test.yaml"
        config_file.write_text("model: RandomForest\nparams: {n_estimators: 100}")
        
        UseCaseManager.load_from_dir(str(config_dir))
        assert UseCaseManager.get_config("test") == {
            "model": "RandomForest",
            "params": {"n_estimators": 100}
        }

class TestDataValidator:
    def test_validate_min_samples(self):
        config = {"data_requirements": {"min_samples": 1000}}
        assert DataValidator.validate(config, {"sample_size": 1500}) is True
        assert DataValidator.validate(config, {"sample_size": 500}) is False
        
    def test_validate_feature_types(self):
        config = {"data_requirements": {"feature_types": ["numerical", "categorical"]}}
        data = {"feature_types": ["numerical", "categorical", "text"]}
        assert DataValidator.validate(config, data) is True
        data = {"feature_types": ["numerical"]}
        assert DataValidator.validate(config, data) is False