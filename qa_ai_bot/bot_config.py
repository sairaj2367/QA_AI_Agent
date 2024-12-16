import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# QA team members
TEAM_MEMBERS = {
    "Queeny": "Host",
    "Sarah": "QA Manager",
    "Alex": "Automation Tester",
    "Emily": "Manual Tester",
    "Michael": "Tech Lead"
}