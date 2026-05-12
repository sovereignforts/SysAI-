import json
import os
from pathlib import Path
from typing import Dict, Any

class Config:
    """Configuration manager for the NLP Chatbot"""
    
    _instance = None
    _config = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if self._config is None:
            self._load_config()
    
    def _load_config(self):
        """Load configuration from settings.json"""
        config_path = Path(__file__).parent / "settings.json"
        
        if config_path.exists():
            with open(config_path, 'r') as f:
                self._config = json.load(f)
        else:
            self._config = self._default_config()
    
    def _default_config(self) -> Dict[str, Any]:
        """Return default configuration"""
        return {
            "app": {"name": "NLP Chatbot", "version": "0.1.0"},
            "database": {"type": "sqlite", "sqlite": {"path": "data/chatbot.db"}},
            "logging": {"level": "INFO"},
        }
    
    def get(self, key: str, default=None):
        """Get configuration value by dot notation (e.g., 'database.type')"""
        keys = key.split('.')
        value = self._config
        
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default
        
        return value if value is not None else default
    
    def set(self, key: str, value: Any):
        """Set configuration value"""
        keys = key.split('.')
        config = self._config
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        config[keys[-1]] = value
    
    def get_all(self) -> Dict[str, Any]:
        """Get entire configuration"""
        return self._config
    
    def save(self):
        """Save configuration to file"""
        config_path = Path(__file__).parent / "settings.json"
        with open(config_path, 'w') as f:
            json.dump(self._config, f, indent=2)


# Create global config instance
config = Config()
