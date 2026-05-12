"""Conversation logging and storage"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any
from src.utils.logger import setup_logger
from src.utils.helpers import ensure_dir

logger = setup_logger(__name__)


class ConversationLogger:
    """Log and store conversations"""
    
    def __init__(self, log_dir: str = "data/conversations/"):
        """Initialize conversation logger"""
        self.log_dir = ensure_dir(log_dir)
        self.buffer = []
        logger.info(f"Conversation logger initialized: {log_dir}")
    
    def log(self, entry: Dict[str, Any]):
        """
        Log a conversation entry
        
        Args:
            entry: Conversation data to log
        """
        try:
            self.buffer.append(entry)
            
            # Flush if buffer is large
            if len(self.buffer) >= 10:
                self.flush()
        
        except Exception as e:
            logger.error(f"Error logging entry: {str(e)}")
    
    def flush(self):
        """Write buffered logs to file"""
        try:
            if not self.buffer:
                return
            
            # Create filename based on date
            date_str = datetime.now().strftime("%Y-%m-%d")
            log_file = self.log_dir / f"conversations_{date_str}.jsonl"
            
            # Append to file
            with open(log_file, 'a', encoding='utf-8') as f:
                for entry in self.buffer:
                    json.dump(entry, f, ensure_ascii=False)
                    f.write('\n')
            
            logger.debug(f"Flushed {len(self.buffer)} log entries")
            self.buffer = []
        
        except Exception as e:
            logger.error(f"Error flushing logs: {str(e)}")
    
    def get_logs(
        self,
        user_id: str = None,
        limit: int = 100,
        date: str = None
    ) -> list:
        """
        Retrieve logged conversations
        
        Args:
            user_id: Filter by user ID
            limit: Maximum number of entries
            date: Filter by date (YYYY-MM-DD)
            
        Returns:
            List of conversation entries
        """
        # TODO: Implement log retrieval
        return []
