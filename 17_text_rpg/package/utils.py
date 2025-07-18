import json
import os

from .models import Player

def load_game():
    if os.path.exists("./save.json"):
        with open("./save.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return Player.from_dict(data)

def save_game(player):
    with open("./save.json", "w", encoding="utf-8") as file:
        json.dump(player.to_dict(), file, indent=4, ensure_ascii=False) #indent = 가독성 좋게 들여쓰기 4칸 #ensure_ascii = 한글 깨지지 않게 해주는