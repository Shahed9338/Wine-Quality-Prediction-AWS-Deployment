import os
from pathlib import Path
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Define project name(local package)
project_name = "myProjet"

# List of files to create or check
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",

    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/data_validation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_evaluation.py",

    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/data_ingestion_pipeline.py",
    f"src/{project_name}/pipeline/data_validation_pipeline.py",
    f"src/{project_name}/pipeline/data_transformation_pipeline.py",
    f"src/{project_name}/pipeline/model_trainer_pipeline.py",
    f"src/{project_name}/pipeline/model_evaluation_pipeline.py",
    f"src/{project_name}/pipeline/prediction_pipeline.py",

    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/utils.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    
    "main.py",
    "app.py",
    "setup.py",
    "requirements.txt",
    "experiments/trials.ipynb",
    "config/config.yaml",
    "params.yaml",
    "Dockerfile",  
]

# Loop through the list of files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create directories if they don't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    # Check if the file doesn't exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # Create an empty file
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")