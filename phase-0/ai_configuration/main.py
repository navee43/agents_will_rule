
from config import load_config , display_config


def main():
     try:
            config = load_config()
            display_config(config)
    
     except ValueError as error:
            print(f"Configuration error: {error}")





if __name__ == "__main__":
      main()

   