import json
import os

from .models import Player

def load_game():
    if os.path.exists("./save.json"):
        with open("./save.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            player = Player.from_dict(data) #from_dict의 반환값(객체)이 player변수에 할당
            return player

def save_game(player):
    with open("./save.json", "w", encoding="utf-8") as file:
        json.dump(player.to_dict(), file, indent=4, ensure_ascii=False)