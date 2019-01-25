
import json
import pyrebase

config = {}

# TODO: Refactor path into ENV variables
with open('matcher/firebase/config.json') as file_config:
    config = json.load(file_config)

firebase = pyrebase.initialize_app(config)

storage = firebase.storage()


def get_csv_file_from_storage(filepath):
    # TODO: Refactor path into ENV variables
    temp_file_path = 'tmp_process/{}'.format(filepath)
    storage.child(filepath).download(temp_file_path)

    return temp_file_path
