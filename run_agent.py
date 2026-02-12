
import sys
import os

# Add the current directory to sys.path so we can import docstring_agent
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from docstring_agent.main import main

if __name__ == "__main__":
    main()
