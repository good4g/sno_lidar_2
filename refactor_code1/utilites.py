import json


def create_memorize_json(**kwargs):
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(kwargs, file)


def check_memorize_json():
    try:
        with open("data.json", encoding="utf-8") as data_js:
            json_settings = json.load(data_js)
            return json_settings
    except FileNotFoundError:
        return False
    except json.decoder.JSONDecodeError:
        return False


