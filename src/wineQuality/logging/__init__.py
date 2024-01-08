import os
import sys
import logging

# Define the logging format string with timestamp, log level, module, and message
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Specify the directory for log files
log_dir = "logs"

# Create a file path for the log file inside the specified directory
log_filepath = os.path.join(log_dir, "running_logs.log")

# Ensure the log directory exists; create it if not
os.makedirs(log_dir, exist_ok=True)

# Configure the logging settings
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO
    format=logging_str,  # Use the defined logging format
    handlers=[
        logging.FileHandler(log_filepath),  # Log to a file
        logging.StreamHandler(sys.stdout)   # Log to the console (stdout)
    ]
)

# Create a logger 
logger = logging.getLogger("wineQualityLogger")