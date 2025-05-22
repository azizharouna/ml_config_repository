import sys
from pathlib import Path
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from core.manager import UseCaseManager

def main():
    try:
        # Load configurations
        config_dir = Path(__file__).parent.parent / "configs"
        UseCaseManager.load_from_dir(str(config_dir))
        
        # Test retrieval
        config = UseCaseManager.get_config("recommendations")
        if config:
            print(f"Successfully loaded configuration:")
            print(f"Model: {config['model']}")
            print(f"Version: {config['version']}")
            return 0
        return 1
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())