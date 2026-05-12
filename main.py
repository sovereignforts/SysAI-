"""
Main entry point for NLP Chatbot application
"""

import sys
from pathlib import Path
from src.utils.logger import setup_logger
from src.chatbot import NLPChatbot

logger = setup_logger(__name__)


def main():
    """Main function to run the chatbot"""
    try:
        logger.info("Initializing NLP Chatbot...")
        
        # Initialize chatbot
        chatbot = NLPChatbot()
        logger.info("Chatbot initialized successfully")
        
        # Start interactive session
        print("\n" + "="*60)
        print("Welcome to NLP Chatbot with Vision & Learning!")
        print("="*60)
        print("Commands:")
        print("  'quit' or 'exit' - Exit the chatbot")
        print("  'mood' - Check detected mood")
        print("  'image <path>' - Analyze an image")
        print("  'help' - Show this help message")
        print("="*60 + "\n")
        
        interactive_chat(chatbot)
        
    except Exception as e:
        logger.error(f"Error starting chatbot: {str(e)}", exc_info=True)
        sys.exit(1)


def interactive_chat(chatbot: NLPChatbot):
    """Run interactive chat session"""
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            # Check for commands
            if user_input.lower() in ['quit', 'exit']:
                print("Chatbot: Goodbye! Thanks for chatting with me!")
                break
            
            elif user_input.lower() == 'help':
                print("\nAvailable commands:")
                print("  'quit' or 'exit' - Exit the chatbot")
                print("  'mood' - Check detected mood")
                print("  'image <path>' - Analyze an image")
                print("  Any other text will be processed as a regular message\n")
            
            elif user_input.lower() == 'mood':
                mood = chatbot.detect_mood(user_input)
                print(f"Chatbot: Detected mood: {mood}\n")
            
            elif user_input.lower().startswith('image '):
                image_path = user_input[6:].strip()
                response = chatbot.analyze_image(image_path, "Analyze this image")
                print(f"Chatbot: {response}\n")
            
            else:
                # Regular chat
                response = chatbot.chat(user_input)
                print(f"Chatbot: {response}\n")
        
        except KeyboardInterrupt:
            print("\n\nChatbot: Goodbye!")
            break
        except Exception as e:
            logger.error(f"Error in chat: {str(e)}")
            print(f"Error: {str(e)}\n")


if __name__ == "__main__":
    main()
