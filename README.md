# NLP Chatbot with Vision & Learning

An intelligent conversational AI that analyzes images, detects user mood, learns from interactions, and improves over time.

## Features

- 🖼️ **Image Analysis**: Upload and analyze images using computer vision
- 💬 **Friendly Chat**: Conversational AI with natural, friendly responses
- 😊 **Mood Detection**: Analyzes user mood from text and images
- 🧠 **Self-Learning**: Learns from user feedback and mistakes
- 💾 **Data Storage**: Persistent storage of conversations and user preferences
- 📊 **Analytics**: Tracks conversation patterns and user preferences
- ⚙️ **Model Training**: Continuously improves with new data

## Project Structure

```
nlp-chatbot/
├── README.md
├── .gitignore
├── requirements.txt
├── setup.py
├── config/
│   ├── __init__.py
│   ├── config.py
│   └── settings.json
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── chatbot.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── nlp_model.py
│   │   ├── vision_model.py
│   │   └── mood_detector.py
│   ├── processors/
│   │   ├── __init__.py
│   │   ├── text_processor.py
│   │   ├── image_processor.py
│   │   └── mood_analyzer.py
│   ├── learning/
│   │   ├── __init__.py
│   │   ├── feedback_handler.py
│   │   ├── model_trainer.py
│   │   └── mistake_learner.py
│   ├── storage/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   ├── conversation_logger.py
│   │   └── user_profile.py
│   └── utils/
│       ├── __init__.py
│       ├── logger.py
│       └── helpers.py
├── data/
│   ├── conversations/
│   ├── user_data/
│   ├── models/
│   └── training_logs/
├── tests/
│   ├── __init__.py
│   ├── test_chatbot.py
│   ├── test_models.py
│   ├── test_processors.py
│   └── test_storage.py
├── notebooks/
│   ├── exploration.ipynb
│   ├── model_training.ipynb
│   └── analysis.ipynb
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
└── scripts/
    ├── train_model.py
    ├── evaluate_model.py
    └── setup_database.py
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/nlp-chatbot.git
   cd nlp-chatbot
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup configuration**
   ```bash
   python scripts/setup_database.py
   ```

5. **Run the chatbot**
   ```bash
   python src/main.py
   ```

## Usage

### Basic Chat
```python
from src.chatbot import NLPChatbot

chatbot = NLPChatbot()
response = chatbot.chat("Hello, how are you?")
print(response)
```

### Image Analysis
```python
response = chatbot.analyze_image("path/to/image.jpg", "Describe this")
print(response)
```

### Mood Detection
```python
mood = chatbot.detect_mood("I'm feeling great today!")
print(f"Detected mood: {mood}")
```

## Configuration

Edit `config/settings.json` to customize:
- API keys and credentials
- Model parameters
- Storage locations
- Learning rates
- Response preferences

## Data & Training

### Conversation Logs
All conversations are stored in `data/conversations/` with timestamps and metadata.

### Model Training
Retrain the model with new data:
```bash
python scripts/train_model.py --data data/conversations/
```

### Evaluation
```bash
python scripts/evaluate_model.py
```

## Technology Stack

- **NLP**: transformers, NLTK, spaCy
- **Vision**: OpenCV, Pillow, PyTorch
- **Database**: SQLite/PostgreSQL
- **Training**: PyTorch/TensorFlow
- **Logging**: Python logging
- **Testing**: pytest, unittest

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Learning Features

### Mood Detection
Analyzes text sentiment and visual cues to understand user emotional state.

### Mistake Learning
When users correct the chatbot, it stores corrections and adjusts responses.

### Continuous Training
Periodic retraining on conversation logs to improve accuracy.

### User Profiling
Learns individual user preferences and conversation styles.

## File Descriptions

- `src/chatbot.py` - Main chatbot orchestrator
- `src/models/` - Core ML models
- `src/processors/` - Input/output processors
- `src/learning/` - Learning and adaptation modules
- `src/storage/` - Data persistence layer
- `data/` - Training data and conversation logs
- `tests/` - Test suite
- `scripts/` - Utility scripts

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Support

For issues and questions, open an issue on GitHub.

---

**Note**: Remember to add your API keys to `.env` file (not committed to version control).
