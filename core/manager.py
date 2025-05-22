from pathlib import Path
import yaml
from typing import Dict, Optional

class UseCaseManager:
    """Central registry for ML configurations with file-based loading"""
    
    _registry: Dict[str, dict] = {}
    
    @classmethod
    def add_config(cls, use_case: str, config: dict) -> None:
        """Register a new use case configuration"""
        cls._registry[use_case] = config
        
    @classmethod
    def get_config(cls, use_case: str, data_profile: dict = None) -> Optional[dict]:
        """Retrieve config if use case exists and data requirements are met"""
        config = cls._registry.get(use_case)
        if not config:
            return None
            
        if data_profile and not DataValidator.validate(config, data_profile):
            return None
            
        return config
        
    @classmethod
    def load_from_dir(cls, config_dir: str) -> None:
        """Load all YAML configs from directory"""
        for config_file in Path(config_dir).glob('**/*.yaml'):
            with open(config_file) as f:
                config = yaml.safe_load(f)
                cls.add_config(config_file.stem, config)


class DataValidator:
    """Validates data against configuration requirements"""
    
    @staticmethod
    def validate(config: dict, data_profile: dict) -> bool:
        requirements = config.get('data_requirements', {})
        
        # Check minimum samples
        if 'min_samples' in requirements:
            if data_profile.get('sample_size', 0) < requirements['min_samples']:
                return False
                
        # Check feature types
        if 'feature_types' in requirements:
            available_types = set(data_profile.get('feature_types', []))
            required_types = set(requirements['feature_types'])
            if not required_types.issubset(available_types):
                return False
                
        return True