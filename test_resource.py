import os
import sys

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
        print(f"Running as PyInstaller executable. Base path: {base_path}")
    except Exception:
        base_path = os.path.abspath(".")
        print(f"Running as Python script. Base path: {base_path}")
    
    full_path = os.path.join(base_path, relative_path)
    print(f"Looking for bg.png at: {full_path}")
    print(f"File exists: {os.path.exists(full_path)}")
    return full_path

# Test the resource path function
bg_path = resource_path("bg.png")
