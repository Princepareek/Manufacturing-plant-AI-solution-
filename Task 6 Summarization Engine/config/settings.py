import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Defaults
CHUNK_SIZE = 2000
CHUNK_OVERLAP = 200
DEFAULT_CHAIN_TYPE = "map_reduce"  # or "refine"
