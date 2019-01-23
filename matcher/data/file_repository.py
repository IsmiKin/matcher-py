import fire
import json
import pyrebase


config = {}
with open('matcher/firebase/config.json') as file_config:
    config = json.load(file_config)

firebase = pyrebase.initialize_app(config)

storage = firebase.storage()


def get_csv_file_from_storage():
    storage.child("sound_recordings_input_report.csv").download('pika.csv')
    url = storage.child("sound_recordings_input_report.csv").get_url(
        config["apiKey"]
        )
    print(url)


fire.Fire()
