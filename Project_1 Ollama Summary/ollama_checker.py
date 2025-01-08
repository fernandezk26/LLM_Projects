import requests
import subprocess
import sys
import os
import time
from pathlib import Path

def get_ollama_path():
    if sys.platform == "win32":
        return str(Path(os.getenv('LOCALAPPDATA')) / "ollama" / "ollama.exe")
    return "ollama"  # Linux/Mac typically install to PATH

def is_ollama_running():
    try:
        response = requests.get("http://localhost:11434/api/version")
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        return False

def ensure_ollama_running():
    if not is_ollama_running():
        try:
            ollama_path = get_ollama_path()
            subprocess.Popen([ollama_path, "serve"], 
                           creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0)
            # Wait for Ollama to start
            for _ in range(10):
                if is_ollama_running():
                    return True
                time.sleep(1)
            return False
        except Exception as e:
            return False
    return True