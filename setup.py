from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="nlp-chatbot",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="An intelligent NLP chatbot with vision, mood detection, and self-learning capabilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/nlp-chatbot",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=[
        "transformers>=4.36.0",
        "torch>=2.1.0",
        "torchvision>=0.16.0",
        "nltk>=3.8",
        "spacy>=3.7.0",
        "opencv-python>=4.8.0",
        "Pillow>=10.0.0",
        "scikit-learn>=1.3.0",
        "pandas>=2.1.0",
        "numpy>=1.24.0",
        "sqlalchemy>=2.0.0",
        "Flask>=3.0.0",
        "FastAPI>=0.104.0",
        "uvicorn>=0.24.0",
        "python-dotenv>=1.0.0",
        "pytest>=7.4.0",
    ],
    extras_require={
        "dev": [
            "black>=23.0.0",
            "flake8>=6.0.0",
            "pylint>=3.0.0",
            "jupyter>=1.0.0",
            "notebook>=7.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "nlp-chatbot=src.main:main",
        ],
    },
)
