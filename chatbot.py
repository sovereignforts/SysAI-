"""
Main NLP Chatbot class that orchestrates all components
"""

from typing import Dict, Optional, Tuple
from datetime import datetime
from src.models.nlp_model import NLPModel
from src.models.vision_model import VisionModel
from src.models.mood_detector import MoodDetector
from src.processors.text_processor import TextProcessor
from src.processors.image_processor import ImageProcessor
from src.processors.mood_analyzer import MoodAnalyzer
from src.storage.conversation_logger import ConversationLogger
from src.storage.user_profile import UserProfile
from src.learning.feedback_handler import FeedbackHandler
from src.utils.logger import setup_logger

logger = setup_logger(__name__)


class NLPChatbot:
    """Main chatbot class combining all NLP and learning capabilities"""
    
    def __init__(self):
        """Initialize all components"""
        logger.info("Initializing NLP Chatbot components...")
        
        # Initialize models
        self.nlp_model = NLPModel()
        self.vision_model = VisionModel()
        self.mood_detector = MoodDetector()
        
        # Initialize processors
        self.text_processor = TextProcessor()
        self.image_processor = ImageProcessor()
        self.mood_analyzer = MoodAnalyzer()
        
        # Initialize storage
        self.conversation_logger = ConversationLogger()
        self.user_profile = UserProfile()
        
        # Initialize learning
        self.feedback_handler = FeedbackHandler()
        
        # Session tracking
        self.current_user_id = None
        self.conversation_history = []
        
        logger.info("All components initialized successfully")
    
    def set_user(self, user_id: str):
        """Set current user"""
        self.current_user_id = user_id
        self.user_profile.load_profile(user_id)
        logger.info(f"User set to: {user_id}")
    
    def chat(self, user_message: str) -> str:
        """
        Main chat method
        
        Args:
            user_message: User's text input
            
        Returns:
            Chatbot's response
        """
        try:
            logger.info(f"Processing user message: {user_message[:50]}...")
            
            # Detect mood
            mood = self.detect_mood(user_message)
            
            # Process text
            processed_text = self.text_processor.process(user_message)
            
            # Generate response
            response = self.nlp_model.generate_response(
                processed_text,
                context=self.conversation_history,
                user_profile=self.user_profile.get_profile() if self.current_user_id else None
            )
            
            # Log conversation
            conversation_entry = {
                "timestamp": datetime.now().isoformat(),
                "user_id": self.current_user_id,
                "user_message": user_message,
                "detected_mood": mood,
                "chatbot_response": response,
                "processed_text": processed_text
            }
            
            self.conversation_logger.log(conversation_entry)
            self.conversation_history.append(conversation_entry)
            
            # Update user profile
            if self.current_user_id:
                self.user_profile.update_interaction(user_message, mood)
            
            logger.info(f"Response generated successfully")
            return response
        
        except Exception as e:
            logger.error(f"Error in chat: {str(e)}", exc_info=True)
            return "I apologize, but I encountered an error. Please try again."
    
    def analyze_image(self, image_path: str, query: Optional[str] = None) -> str:
        """
        Analyze uploaded image
        
        Args:
            image_path: Path to image file
            query: Optional query about the image
            
        Returns:
            Analysis result
        """
        try:
            logger.info(f"Analyzing image: {image_path}")
            
            # Process image
            image_data = self.image_processor.load_image(image_path)
            features = self.vision_model.extract_features(image_data)
            
            # Generate description
            description = self.vision_model.generate_description(features)
            
            # If query provided, answer it
            answer = description
            if query:
                answer = self.vision_model.answer_question(features, query)
            
            # Log interaction
            if self.current_user_id:
                self.conversation_logger.log({
                    "timestamp": datetime.now().isoformat(),
                    "user_id": self.current_user_id,
                    "type": "image_analysis",
                    "image_path": image_path,
                    "query": query,
                    "result": answer
                })
            
            logger.info("Image analysis completed")
            return answer
        
        except Exception as e:
            logger.error(f"Error analyzing image: {str(e)}", exc_info=True)
            return "I couldn't analyze the image. Please check the file path."
    
    def detect_mood(self, text: str) -> str:
        """
        Detect user mood from text
        
        Args:
            text: User text
            
        Returns:
            Detected mood label
        """
        try:
            mood = self.mood_analyzer.analyze_text(text)
            logger.debug(f"Detected mood: {mood}")
            return mood
        except Exception as e:
            logger.error(f"Error detecting mood: {str(e)}")
            return "neutral"
    
    def provide_feedback(self, conversation_id: str, feedback: str, rating: float):
        """
        Handle user feedback for learning
        
        Args:
            conversation_id: ID of conversation entry
            feedback: User's feedback text
            rating: Rating (0-1 scale)
        """
        try:
            logger.info(f"Processing feedback for conversation: {conversation_id}")
            self.feedback_handler.process_feedback(
                conversation_id,
                feedback,
                rating,
                self.current_user_id
            )
            logger.info("Feedback processed successfully")
        except Exception as e:
            logger.error(f"Error processing feedback: {str(e)}", exc_info=True)
    
    def get_conversation_history(self, limit: int = 10) -> list:
        """Get recent conversation history"""
        return self.conversation_history[-limit:]
    
    def save_session(self):
        """Save current session data"""
        try:
            logger.info("Saving session...")
            if self.current_user_id:
                self.user_profile.save_profile()
            self.conversation_logger.flush()
            logger.info("Session saved successfully")
        except Exception as e:
            logger.error(f"Error saving session: {str(e)}", exc_info=True)
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
        logger.info("Conversation history cleared")
