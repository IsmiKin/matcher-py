import time

from data.logic import get_all_sound_recordings

def main():
    while True:
        time.sleep(1)
        sound_recordings = get_all_sound_recordings()
        for record in sound_recordings:
            print(record.id)

        print("Hello World!")

main()
