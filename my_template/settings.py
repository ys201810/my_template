import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = Path.cwd().parent / 'env_file' / '.env.work'
if dotenv_path.exists():
    load_dotenv(dotenv_path)
else:
    print("No .env file found in the project root directory")
    exit(1)

EXAMPLE = os.environ.get("EXAMPLE")
