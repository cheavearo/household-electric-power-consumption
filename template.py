import os
from pathlib import Path 
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name="household-electric-power-consumption"

list_of_files=[
    ".gthub/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "setup.py",
    "research/research.ipynb",
    "templates/index.html",
    "app.py"

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename=os.path.split(filepath)

    ## If file dictory does not exist, create this directory with its {filename}
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Created {filedir} directory for {filename} is done")
        '''
        * If the filedir is not an empty string (i.e., it’s not a file in the root directory),
        * It creates the directory (and any missing parent directories) if it doesn't already exist.
        * exist_ok=True prevents errors if the directory already exists.
        * It logs a message saying it's ensuring the directory is ready.
        '''
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath))==0:
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empy file: {filepath}")
        '''
        - If the file does not exist OR it exists but is empty (size 0 bytes):
        - It creates an empty file (using with open(..., "w")).
        - Logs that it created the file.
        '''
    else:
        logging.info(f" {filename} is already existed!")

