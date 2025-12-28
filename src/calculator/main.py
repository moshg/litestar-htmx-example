from calculator.add import add
from calculator.logger import logger


def main() -> None:
    logger.info("Starting main function")
    s = add(1, 2)
    print(f"Sum is {s}")
    logger.info("Ending main function")


if __name__ == "__main__":
    main()
