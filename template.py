import os
import sys
import time
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s: ")
package_name = "deepClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f'src/{package_name}/__init__.py',
    f'src/{package_name}/components/__init__.py',
    f'src/{package_name}/utils/__init__.py',
    f'src/{package_name}/config/__init__.py',
    f'src/{package_name}/pipeline/__init__.py',
    f'src/{package_name}/constants/__init__.py',
    "configs/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir}")