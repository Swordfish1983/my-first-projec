import logging
import sys
from datetime import datetime


APP_NAME = "Simple VPN"
VERSION = "0.1.0"


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )


def startup():
    logging.info(f"{APP_NAME} v{VERSION}")
    logging.info(f"Started at: {datetime.now()}")


def shutdown():
    logging.info("Application closed.")


def main():
    setup_logging()
    startup()

    try:
        print("=" * 40)
        print(f"{APP_NAME} v{VERSION}")
        print("=" * 40)

        print("Status : Ready")
        print("Server : Not Connected")
        print("Mode   : Development")

        # Future implementation:
        # - Load configuration
        # - Connect to server
        # - Start secure session
        # - Monitor connection

    except KeyboardInterrupt:
        print("\nInterrupted by user.")

    except Exception as e:
        logging.error(f"Error: {e}")

    finally:
        shutdown()


if __name__ == "__main__":
    sys.exit(main())
