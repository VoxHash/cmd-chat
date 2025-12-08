#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Run script for cmd-chat
Provides convenient entry point for running the application
"""
import sys
import os
import subprocess
from pathlib import Path

# Set UTF-8 encoding for Windows compatibility
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

def check_venv():
    """Check if virtual environment is activated"""
    # Check for virtual environment indicators
    in_venv = (
        hasattr(sys, 'real_prefix') or
        (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix) or
        os.environ.get('VIRTUAL_ENV') is not None
    )
    return in_venv

def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        import sanic
        import requests
        import rsa
        import cryptography
        import colorama
        import pydantic
        import websocket
        import rich
        import dotenv
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e.name}")
        print("💡 Run: pip install -r requirements.txt")
        return False

def main():
    """Main entry point"""
    # Check virtual environment
    if not check_venv():
        print("⚠️  Warning: Virtual environment not detected")
        print("💡 Recommended: python -m venv venv && source venv/bin/activate (Linux/Mac)")
        print("💡 Recommended: python -m venv venv && .\\venv\\Scripts\\activate (Windows)")
        print()
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Import and run cmd_chat
    try:
        import cmd_chat
        import asyncio
        
        # Run the async main function
        asyncio.run(cmd_chat.run())
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()

