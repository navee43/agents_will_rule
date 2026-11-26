import os
from dotenv import load_dotenv
from pathlib import Path



BASE_DIR = Path(__file__).parent
ENV_FILE = BASE_DIR/".env"
load_dotenv(ENV_FILE)


def load_config():

    APP_NAME = os.getenv("APP_NAME", "AI Assistant")
    MODEL_NAME = os.getenv("MODEL_NAME", "default-model")
    MAX_ITERATIONS = int(os.getenv("MAX_ITERATIONS", "5"))
    TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
    API_KEY = os.getenv("API_KEY")

    if not API_KEY or not API_KEY.strip():
        raise ValueError("API key is not configured")

    if MAX_ITERATIONS <= 0:
        raise ValueError("Maximum iterations must be positive")

    if not 0 <= TEMPERATURE <= 1:
        raise ValueError("Temperature must be between 0 and 1")

    config = {
        "APP_NAME": APP_NAME,
        "MODEL_NAME": MODEL_NAME,
        "MAX_ITERATIONS": MAX_ITERATIONS,
        "TEMPERATURE": TEMPERATURE,
        "API_KEY": API_KEY
    }

    return config


def display_config(config):

    print("===== AI Agent Configuration =====")

    for key, value in config.items():
        if key == "API_KEY":
            print(f"{key}: Configured")
        else:
            print(f"{key}: {value}")


