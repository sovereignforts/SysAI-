#!/usr/bin/env python
"""
Script to setup the database
"""

import argparse
from pathlib import Path
from src.storage.database import init_db
from src.utils.logger import setup_logger

logger = setup_logger(__name__)


def main():
    """Main database setup"""
    parser = argparse.ArgumentParser(description="Setup chatbot database")
    parser.add_argument(
        "--db-type",
        type=str,
        choices=["sqlite", "postgresql"],
        default="sqlite",
        help="Database type"
    )
    parser.add_argument(
        "--db-path",
        type=str,
        default="data/chatbot.db",
        help="Database path (for SQLite)"
    )
    parser.add_argument(
        "--reset",
        action="store_true",
        help="Reset database (delete existing)"
    )
    
    args = parser.parse_args()
    
    try:
        db_path = Path(args.db_path)
        
        # Handle reset
        if args.reset and db_path.exists():
            logger.info(f"Resetting database: {args.db_path}")
            db_path.unlink()
        
        logger.info(f"Initializing database: {args.db_type}")
        
        # Initialize database
        db = init_db(args.db_type, args.db_path)
        
        # Create required directories
        Path("data/conversations").mkdir(parents=True, exist_ok=True)
        Path("data/user_data").mkdir(parents=True, exist_ok=True)
        Path("data/models").mkdir(parents=True, exist_ok=True)
        Path("data/training_logs").mkdir(parents=True, exist_ok=True)
        Path("logs").mkdir(parents=True, exist_ok=True)
        
        logger.info("Database setup completed successfully!")
        print("\n✓ Database initialized")
        print(f"  Type: {args.db_type}")
        print(f"  Path: {args.db_path}")
        print("\n✓ Directories created:")
        print("  - data/conversations/")
        print("  - data/user_data/")
        print("  - data/models/")
        print("  - data/training_logs/")
        print("  - logs/")
        
    except Exception as e:
        logger.error(f"Database setup failed: {str(e)}", exc_info=True)
        print(f"\n✗ Setup failed: {str(e)}")
        exit(1)


if __name__ == "__main__":
    main()
