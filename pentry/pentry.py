# pentry.py

import argparse
from datetime import datetime 
import os

from .utils.config_loader import load_folder_structure
from .utils.create_directory import create_directory
from .utils.logger import get_logger

logger = get_logger("pentry")

DESCRIPTION = "Scaffold a pentest project structure."

def create_root_directory(name: str, base_path: str, date: str) -> str:
    folder_name = f"{name}_{date}"
    root_path = os.path.join(base_path, folder_name)
    logger.info(f"Creating root directory at: {root_path}")
    created_path = create_directory(root_path)
    logger.debug(f"Root directory created: {created_path}")
    return created_path

def scaffold_project_folders(root_path: str, folders: str) -> None:
    for folder in folders:
        full_path = os.path.join(root_path, folder)
        logger.info(f"Creating project folder: {full_path}")
        created_folder = create_directory(full_path)
        logger.debug(f"Project folder created: {created_folder}")

def main():
    parser = argparse.ArgumentParser(DESCRIPTION)

    parser.add_argument("name", help="Name of the engagement (e.g., 'acme-inc')")
    parser.add_argument("--output", default=".", help="Base output path (default: current directory)")
    parser.add_argument("--template", default="default", help="Folder template to use (default: 'default')")
    parser.add_argument("--date", default=datetime.now().strftime("%Y-%m-%d"), help="Engagement date (default: today)")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")

    args = parser.parse_args()

    if args.debug:
        logger.setLevel(10)  
        logger.debug("Debug logging enabled")
    
    logger.info(f"Starting project scaffold for '{args.name}' on {args.date} using template '{args.template}'")

    # Step 1: Create base directory
    try: 
        root_path = create_root_directory(args.name, args.output, args.date)
    except Exception as e:
        logger.error(f"Failed to create root directory: {e}")
        return

    # Step 2: Scaffold project folders
    try:
        folder_structure = load_folder_structure(args.template)
        scaffold_project_folders(root_path, folder_structure)
    except Exception as e:
        logger.error(f"Failed to scaffold project folders: {e}")
        return

if __name__ == "__main__":
    try:
        logger.info("Starting pentry project scaffold")
        main()
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise
    else:
        logger.info("Pentry project scaffold completed successfully")
