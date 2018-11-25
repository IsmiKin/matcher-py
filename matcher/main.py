import time
import logging

from data.logic import get_all_sound_recordings

FORMAT = "[%(asctime)s][%(levelname)-5.5s] %(message)s"
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.INFO)

def main():
    while True:
        time.sleep(1)
        sound_recordings = get_all_sound_recordings()
        for record in sound_recordings:
            # print(record.id)
            log.info('PRINTING RECORD:{}'.format(record.id))

main()
