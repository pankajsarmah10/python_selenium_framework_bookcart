import logging
import os
from datetime import datetime


class Logger:
    _loggers = {}

    def __init__(self):
        # No need to initialize anything here
        pass

    def get_logger(self, worker_id=None):
        """Get or create a logger instance"""
        logger_name = f"pytest-selenium-logger-{worker_id or 'default'}"

        # Return existing logger if already created
        if logger_name in self._loggers:
            return self._loggers[logger_name]

        # Create new logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)

        # Only add handlers if none exist
        if not logger.handlers:
            # Create logs directory
            root_dir = os.path.dirname(os.path.abspath(__file__))
            root_dir = os.path.abspath(os.path.join(root_dir, ".."))
            logs_dir = os.path.join(root_dir, "logs")
            os.makedirs(logs_dir, exist_ok=True)

            # Create log file
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            log_file = os.path.join(
                logs_dir,
                f"test_log_{timestamp}_{worker_id or 'default'}.log"
            )

            # File handler
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(logging.DEBUG)

            # Console handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.DEBUG)

            # Formatter
            formatter = logging.Formatter(
                '%(asctime)s - [%(name)s] - %(levelname)s - %(message)s'
            )

            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            logger.addHandler(console_handler)
            logger.propagate = False

        self._loggers[logger_name] = logger
        return logger