import os
from pathlib import Path
import logging

project_name = 'SafetyTrack'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"{project_name}/data/images/train",
    f"{project_name}/data/images/val",
    f"{project_name}/data/label/train",
    f"{project_name}/data/label/val",
    f"{project_name}/config/metro.yaml",
    f"{project_name}/train.py",
    f"{project_name}/test.py",
    f"{project_name}/detect.py",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")