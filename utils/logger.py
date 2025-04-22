import logging

# Configure the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
_console_handler = logging.StreamHandler()
_console_handler.setLevel(logging.DEBUG)
_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
_console_handler.setFormatter(_formatter)
logger.addHandler(_console_handler)

# TODO: Optionally allow configuration of log level, handlers, format, etc.


def log_debug(message: str) -> None:
    """
    Logs a debug-level message.

    :param message: The message to log.
    :raises TypeError: If the message is not a string.
    """
    if not isinstance(message, str):
        raise TypeError("Message must be a string.")
    logger.debug(message)


def log_info(message: str) -> None:
    """
    Logs an informational message.

    :param message: The message to log.
    :raises TypeError: If the message is not a string.
    """
    if not isinstance(message, str):
        raise TypeError("Message must be a string.")
    logger.info(message)


def log_error(message: str) -> None:
    """
    Logs an error message.

    :param message: The message to log.
    :raises TypeError: If the message is not a string.
    """
    if not isinstance(message, str):
        raise TypeError("Message must be a string.")
    logger.error(message)