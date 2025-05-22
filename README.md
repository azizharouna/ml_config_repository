# ML Configuration Repository

[![Tests](https://github.com/azizharouna/ml-config-repo/actions/workflows/tests.yml/badge.svg)](https://github.com/azizharouna/ml-config-repo/actions)
[![Coverage](https://img.shields.io/badge/coverage-95%25-brightgreen)](https://azizharouna.github.io/ml-config-repo/coverage)

Centralized configuration management system for machine learning use cases.

## Features

- **Versioned configurations** - Track model parameters and requirements
- **Validation engine** - Ensure data meets requirements before use
- **Registry system** - Central access to all configurations
- **YAML-based** - Human-readable configuration format

## Quick Start

```bash
# Install
pip install -r requirements-test.txt

# Load configurations
python scripts/register_configs.py configs/

# Run tests
make test
```

## Project Structure

```
ml_config_repository/
├── configs/              # YAML configuration files
├── core/                 # Core manager and validator
├── tests/                # Unit and integration tests
├── scripts/              # Utility scripts
├── docs/                 # Documentation
└── examples/             # Usage examples
```

## Configuration Example

```yaml
# configs/ecommerce/recommendations.yaml
model: XGBoost
version: 2.1.0
parameters:
  max_depth: 8
  learning_rate: 0.1
data_requirements:
  min_samples: 10000
  feature_types: [numerical, categorical]
```

## Documentation

- [API Reference](docs/api_reference.md)
- [Configuration Spec](docs/config_spec.md)
- [CLI Usage](docs/cli_usage.md)
- [Deployment Guide](docs/deployment.md)

## Development

```bash
# Run linter
make lint

# Generate coverage report
make test-cov

# Run all checks
make ci
```

## License

MIT