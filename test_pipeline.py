
import sys
import os
from docstring_agent.main import run_processing_pipeline
from docstring_agent.utils.config_manager import ConfigManager

try:
    print("Starting Pipeline Test...")
    config = ConfigManager()
    key = config.get_api_key()
    print(f"API Key present: {bool(key)}")
    
    run_processing_pipeline(
        input_path="d:/Drive D/nasiko/temp_uploads/main.py",
        style="google",
        dry_run=False,
        model="gpt-4o",
        api_key=key,
        base_url=None,
        interaction_agent=None,
        verbose=True
    )
    print("Pipeline Test Complete!")
except Exception as e:
    print(f"Pipeline Crashed: {e}")
    import traceback
    traceback.print_exc()
