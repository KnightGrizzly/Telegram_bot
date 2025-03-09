import json


def get_data(file_path: str):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

if __name__ == "__main__":
    get_data("../data.json")