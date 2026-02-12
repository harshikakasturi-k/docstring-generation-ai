
import sys
import os
import uvicorn

# Ensure the current directory is in sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    print("🚀 Launching AI 3D World...")
    print("🌍 Open http://localhost:8000 in your browser")
    
    # Import app object string to allow reloading
    uvicorn.run("app_server:app", host="127.0.0.1", port=8000, reload=True)
