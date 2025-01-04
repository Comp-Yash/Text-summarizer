'''
this give our file , so that this script run and we dont need to create files and folder to save time 

its more planned and structural way 

'''

import os 
from pathlib import Path 
import logging 



logging.basicConfig(
    level=logging.INFO,  # Use INFO in uppercase
    format='[%(asctime)s]:%(message)s:'  # Corrected 'formate' to 'format'
)


project_name="textsummarizer"
#pipeline
list_of_file=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging//__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/configuration.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
   

    


]


for filepath in list_of_file:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating dir: {filedir} for file {filename}")
    if (not os.path.exists(filepath)) or  (os.path.getsize(filepath)==0):
        with filepath.open('w'):
            logging.info(f"Creating file: {filepath}")
            pass
    else:
        logging.info(f"{filename} file already exits ")



















