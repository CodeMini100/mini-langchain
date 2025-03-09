import logging

def setup_logger(name: str = "langchain", level=logging.DEBUG) -> logging.Logger:
    """
    Set up and return a logger.
    TODO:
      - Create a stream handler and a file handler.
      - Use a formatter for detailed messages.
      - Allow for adjustable verbosity.
    Hint:
      handler = logging.StreamHandler()
      formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
      handler.setFormatter(formatter)
      logger.addHandler(handler)
    """
    pass
