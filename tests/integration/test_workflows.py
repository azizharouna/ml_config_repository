import pytest
import yaml
from pathlib import Path
from ..core.manager import UseCaseManager

class TestIntegrationWorkflows:
    @pytest.fixture
    def sample_config_dir(self, tmp_path):
        config_dir = tmp_path / "configs"
        config_dir.mkdir()
        
        # Create ecommerce config
        (config_dir / "ecommerce").mkdir()
        (config_dir / "ecommerce" / "recommendations.yaml").write_text("""
        model: XGBoost
        data_requirements:
          min_samples: 1000
        """)
        
        # Create trust_safety config
        (config_dir / "trust_safety").mkdir()
        (config_dir / "trust_safety" / "fraud.yaml").write_text("""
        model: RandomForest
        data_requirements:
          min_samples: 5000
        """)
        
        return str(config_dir)

    def test_config_loading_workflow(self, sample_config_dir):
        UseCaseManager.load_from_dir(sample_config_dir)
        
        # Test ecommerce config
        ecom_config = UseCaseManager.get_config(
            "recommendations",
            {"sample_size": 1500}
        )
        assert ecom_config["model"] == "XGBoost"
        
        # Test trust_safety config
        fraud_config = UseCaseManager.get_config(
            "fraud", 
            {"sample_size": 6000}
        )
        assert fraud_config["model"] == "RandomForest"
        
        # Test failed validation
        assert UseCaseManager.get_config(
            "recommendations",
            {"sample_size": 500}
        ) is None