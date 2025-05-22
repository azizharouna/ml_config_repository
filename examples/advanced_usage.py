import sys
from pathlib import Path
from ..core.manager import UseCaseManager

def main():
    try:
        # Load from configs directory
        config_dir = Path(__file__).parent.parent / "configs"
        print(f"Loading configs from: {config_dir}")
        UseCaseManager.load_from_dir(str(config_dir))
        
        # Example data profile
        data_profile = {
            "sample_size": 8000,
            "feature_types": ["numerical", "categorical"]
        }

        # Get config with validation
        print("\nAttempting to load 'recommendations' config...")
        config = UseCaseManager.get_config(
            "recommendations",
            data_profile=data_profile
        )

        if not config:
            print("Error: Invalid config or data requirements not met")
            return 1

        print(f"\nSuccessfully loaded config:")
        print(f"Model: {config['model']}")
        print(f"Version: {config['version']}")
        return 0

    except Exception as e:
        print(f"\nError: {str(e)}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())