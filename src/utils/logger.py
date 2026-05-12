"""
Logging configuration for the chatbot
"""

import logging
import sys
from pathlib import Path
from logging.handlers import RotatingFileHandler


def setup_logger(name: str, log_level=logging.INFO) -> logging.Logger:
    """
    Setup logger with both file and console handlers
    
    Args:
        name: Logger name
        log_level: Logging level
        
    Returns:
        Configured logger instance
    """
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    
    # Prevent duplicate handlers
    if logger.hasHandlers():
        return logger
    
    # Create logs directory if it doesn't exist
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    # Create formatters
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)
    
    # File handler with rotation
    file_handler = RotatingFileHandler(
        log_dir / 'chatbot.log',
        maxBytes=10485760,  # 10MB
        backupCount=5
    )
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)
    
    # Add handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger


# Global logger for quick access
logger = setup_logger(__name__)
