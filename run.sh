#!/bin/bash
# Run script for cmd-chat (Unix/Linux/macOS)

set -e

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}⚠️  Virtual environment not found${NC}"
    echo -e "${GREEN}💡 Creating virtual environment...${NC}"
    python3 -m venv venv
fi

# Activate virtual environment
echo -e "${GREEN}🔌 Activating virtual environment...${NC}"
source venv/bin/activate

# Check if dependencies are installed
if ! python -c "import sanic" 2>/dev/null; then
    echo -e "${YELLOW}⚠️  Dependencies not installed${NC}"
    echo -e "${GREEN}💡 Installing dependencies...${NC}"
    pip install -r requirements.txt
fi

# Run the application
echo -e "${GREEN}🚀 Starting cmd-chat...${NC}"
python run.py "$@"

