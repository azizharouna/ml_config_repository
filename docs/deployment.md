# Deployment Guide v2.1

## Production Setup
1. **Dependencies**:
```bash
pip install PyYAML>=6.0.1
```

2. **Configuration Loading**:
```python
from core.manager import UseCaseManager

# Load during application startup
UseCaseManager.load_from_dir("/etc/ml_configs")

# Runtime usage
config = UseCaseManager.get_config(
    "fraud_detection",
    {"sample_size": 10000}
)
```

## CI/CD Pipeline
```yaml
# Sample GitHub Actions workflow
name: CI
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
      - name: Install dependencies
        run: pip install -r requirements-test.txt
      - name: Run tests
        run: make ci
```

## Monitoring
| Metric | Description | Alert Threshold |
|--------|-------------|------------------|
| Config Load Errors | Failed config loads | >1% of requests |
| Cache Hit Rate | Registry cache efficiency | <90% |
| Validation Time | Requirement checks | >500ms |

## Version Control
```bash
# Recommended pre-commit hook
repos:
- repo: local
  hooks:
    - id: validate-configs
      name: Validate YAML configs
      entry: python scripts/validate_configs.py
      files: \.yaml$