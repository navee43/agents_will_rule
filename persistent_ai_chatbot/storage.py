import os
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR=BASE_DIR/"data"

DATA_DIR.mkdir(exist_ok=True)
HISTORY_FILE=DATA_DIR/"history.json"



def load_history():

  try:
    with open(HISTORY_FILE,"r",encoding="utf-8") as file:
      data = json.load(file)
    if not isinstance(data,list):
       raise ValueError("data is corrupted")
    return data
  except FileNotFoundError:
             return []
  

def save_history(messages):
  with open(HISTORY_FILE,"w",encoding="utf-8") as file:
   json.dump(messages,file,indent=4)


def clear_history():
   save_history([])
    