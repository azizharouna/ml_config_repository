# API Reference v2.1

## Core Components

### `UseCaseManager`
```python
class UseCaseManager:
    """Central configuration registry for ML use cases"""
    
    @classmethod
    def add_config(cls, use_case: str, config: dict) -> None:
        """Register a new configuration
        
        Args:
            use_case: Unique identifier (e.g. "ecommerce_recommendations")
            config: Dictionary containing model params and data requirements
        """
        
    @classmethod
    def get_config(cls, use_case: str, data_profile: dict = None) -> Optional[dict]:
        """Retrieve configuration if requirements are met
        
        Args:
            use_case: Configuration identifier
            data_profile: Dictionary of available data characteristics
                          (e.g. {"sample_size": 5000})
                          
        Returns:
            Configuration dict or None if requirements not met
        """
        
    @classmethod
    def load_from_dir(cls, config_dir: str) -> None:
        """Load all YAML configs from directory
        
        Args:
            config_dir: Path containing YAML config files
        """
```

### `DataValidator`
```python
class DataValidator:
    """Validation engine for configuration requirements"""
    
    @staticmethod
    def validate(config: dict, data_profile: dict) -> bool:
        """Check if data meets configuration requirements
        
        Args:
            config: Configuration dictionary
            data_profile: Available data characteristics
            
        Returns:
            True if all requirements are satisfied
        """
```

## Example Workflow

```python
# Initialize
from core.manager import UseCaseManager
UseCaseManager.load_from_dir("configs/")

# Get validated config
config = UseCaseManager.get_config(
    "recommendations",
    {"sample_size": 10000, "feature_types": ["numerical"]}
)
```

## Error Handling

| Error Case | Exception | Recommended Action |
|------------|-----------|--------------------|
| Invalid YAML | `yaml.YAMLError` | Check file syntax |
| Missing Requirements | `None` returned | Verify data profile |
| Permission Denied | `PermissionError` | Check file access |