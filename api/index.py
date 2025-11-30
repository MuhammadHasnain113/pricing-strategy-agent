"""
Vercel serverless function entry point for FastAPI application
"""
import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.main import app

# Vercel expects the handler to be named 'handler' or 'app'
# For FastAPI/ASGI apps, we export the app directly
handler = app
