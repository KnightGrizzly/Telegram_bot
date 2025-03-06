import json
# from typing import Optional


def get_data(file_path: str):
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        print(data)


if __name__ == "__main__":
    get_data("data.json")