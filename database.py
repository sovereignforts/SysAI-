"""Database connection and ORM setup"""

from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

# Create base for ORM models
Base = declarative_base()


class Database:
    """Database manager"""
    
    def __init__(self, db_type: str = "sqlite", db_path: str = "data/chatbot.db"):
        """
        Initialize database connection
        
        Args:
            db_type: Type of database (sqlite, postgresql)
            db_path: Path to database file (for SQLite)
        """
        self.db_type = db_type
        self.db_path = db_path
        self.engine = None
        self.Session = None
        
        self._init_connection()
    
    def _init_connection(self):
        """Initialize database connection"""
        try:
            if self.db_type == "sqlite":
                # Ensure directory exists
                Path(self.db_path).parent.mkdir(parents=True, exist_ok=True)
                connection_string = f"sqlite:///{self.db_path}"
            else:
                raise ValueError(f"Unsupported database type: {self.db_type}")
            
            self.engine = create_engine(connection_string, echo=False)
            self.Session = sessionmaker(bind=self.engine)
            
            logger.info(f"Database connection initialized: {self.db_type}")
        except Exception as e:
            logger.error(f"Failed to initialize database: {str(e)}")
            raise
    
    def create_tables(self):
        """Create all tables"""
        try:
            Base.metadata.create_all(self.engine)
            logger.info("Database tables created")
        except Exception as e:
            logger.error(f"Error creating tables: {str(e)}")
            raise
    
    def get_session(self):
        """Get database session"""
        if self.Session is None:
            raise RuntimeError("Database not initialized")
        return self.Session()
    
    def close(self):
        """Close database connection"""
        if self.engine:
            self.engine.dispose()
            logger.info("Database connection closed")


# Global database instance
db = None


def init_db(db_type: str = "sqlite", db_path: str = "data/chatbot.db"):
    """Initialize global database instance"""
    global db
    db = Database(db_type, db_path)
    db.create_tables()
    return db


def get_db() -> Database:
    """Get global database instance"""
    global db
    if db is None:
        db = init_db()
    return db
