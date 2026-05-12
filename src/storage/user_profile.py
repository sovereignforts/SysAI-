"""User profile and preference management"""

import json
from pathlib import Path
from typing import Dict, Any
from src.utils.logger import setup_logger
from src.utils.helpers import ensure_dir, load_json, save_json

logger = setup_logger(__name__)


class UserProfile:
    """Manage user profiles and preferences"""
    
    def __init__(self, profiles_dir: str = "data/user_data/"):
        """Initialize user profile manager"""
        self.profiles_dir = ensure_dir(profiles_dir)
        self.current_user_id = None
        self.profile_data = {}
        logger.info(f"User profile manager initialized: {profiles_dir}")
    
    def load_profile(self, user_id: str):
        """Load user profile"""
        try:
            self.current_user_id = user_id
            profile_path = self.profiles_dir / f"{user_id}.json"
            
            if profile_path.exists():
                self.profile_data = load_json(str(profile_path))
            else:
                self.profile_data = self._create_default_profile(user_id)
            
            logger.info(f"Loaded profile for user: {user_id}")
        
        except Exception as e:
            logger.error(f"Error loading profile: {str(e)}")
            self.profile_data = self._create_default_profile(user_id)
    
    def _create_default_profile(self, user_id: str) -> Dict[str, Any]:
        """Create default user profile"""
        return {
            "user_id": user_id,
            "created_at": str(Path.ctime(Path('.'))),
            "conversation_count": 0,
            "mood_history": [],
            "preferences": {
                "language": "english",
                "tone": "friendly",
                "verbose": True
            },
            "interactions": []
        }
    
    def save_profile(self):
        """Save current profile to disk"""
        try:
            if not self.current_user_id:
                logger.warning("No user loaded")
                return
            
            profile_path = self.profiles_dir / f"{self.current_user_id}.json"
            save_json(self.profile_data, str(profile_path))
            logger.info(f"Profile saved for user: {self.current_user_id}")
        
        except Exception as e:
            logger.error(f"Error saving profile: {str(e)}")
    
    def get_profile(self) -> Dict[str, Any]:
        """Get current user profile"""
        return self.profile_data
    
    def update_interaction(self, message: str, mood: str):
        """Track user interaction"""
        try:
            if "interactions" not in self.profile_data:
                self.profile_data["interactions"] = []
            
            self.profile_data["interactions"].append({
                "message": message,
                "mood": mood,
                "timestamp": str(Path.ctime(Path('.')))
            })
            
            self.profile_data["conversation_count"] = \
                self.profile_data.get("conversation_count", 0) + 1
        
        except Exception as e:
            logger.error(f"Error updating interaction: {str(e)}")
    
    def set_preference(self, key: str, value: Any):
        """Set user preference"""
        if "preferences" not in self.profile_data:
            self.profile_data["preferences"] = {}
        
        self.profile_data["preferences"][key] = value
