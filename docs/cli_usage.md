# CLI Usage Guide

## Register Configurations
```bash
python scripts/register_configs.py path/to/configs
```

## Run Tests
```bash
# Install dependencies
pip install -r requirements-test.txt

# Run all tests with coverage
make test

# Run specific test module
pytest tests/unit/test_manager.py -v
```

## Linting
```bash
make lint  # Uses flake8
```

## Example Workflow
```bash
# 1. Register configurations
python scripts/register_configs.py configs/

# 2. Run validation tests
pytest tests/integration/test_workflows.py

# 3. Generate coverage report
pytest --cov-report=html