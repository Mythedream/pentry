from utils.logger import get_logger

logger = get_logger("pentry")

def main():
    logger.info("Pentry script started.")
    # Add your main logic here
    try:
        # Simulate some processing
        logger.debug("Processing data...")
        # More processing...
        logger.info("Processing completed successfully.")
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()