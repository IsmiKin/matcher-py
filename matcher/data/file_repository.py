import fire

import firebase_admin
from firebase_admin import credentials, storage


cred = credentials.Certificate('matcher/creds/.firebase-creds.json')

firebase_app = firebase_admin.initialize_app(
    cred,
    {'storageBucket': 'matcher-py.appspot.com'}
)

bucket = storage.bucket(app=firebase_app)


def get_csv_file_from_storage():
    blob = bucket.blob("sound_recordings_input_report.csv")
    print(blob)


# def main():
fire.Fire()


# main()
