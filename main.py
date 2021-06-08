from pathlib import Path
import sys

dir_path = sys.argv[1]
dir_path = Path(dir_path)

for items in dir_path.iterdir():
    print(items.is_file())
