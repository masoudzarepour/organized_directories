from pathlib import Path
import sys
import shutil

dir_path = sys.argv[1]
dir_path = Path(dir_path)

for item in dir_path.iterdir():

    if not item.is_file():
        continue

    if item.suffix.lower() in ['.jpg', '.mp4', '.ttf']:
        #print(item, Path(dir_path,'Images&Videos'))
        shutil.move(str(item), str(Path(dir_path,'Images&Videos')))

