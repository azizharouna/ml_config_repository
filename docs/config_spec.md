# Configuration Specification v2.1

## Required Fields
```yaml
model: string  # Algorithm name (e.g. "XGBoost")
version: string  # Semantic version (e.g. "1.0.0")
```

## Optional Sections

### Parameters
```yaml
parameters:  # Model-specific parameters
  param1: value
  param2: value
```

### Data Requirements
```yaml
data_requirements:
  min_samples: integer  # Minimum sample size
  feature_types:  # Required feature types
    - string  # e.g. "numerical", "categorical"
  required_columns:  # Mandatory columns
    - string
```

### Metadata
```yaml
metadata:
  owner: string  # Team/individual responsible
  last_tested: date  # YYYY-MM-DD
  performance:  # Key metrics
    metric1: float
    metric2: float
```

## Example Config
```yaml
model: RandomForest
version: 2.1.0
parameters:
  n_estimators: 200
  max_depth: 12
data_requirements:
  min_samples: 10000
  feature_types: [numerical, categorical]
metadata:
  owner: fraud-team
  last_tested: 2024-05-18
  performance:
    precision: 0.92
    recall: 0.88