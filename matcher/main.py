import time
import logging
import fire

from data.logic import get_all_sound_recordings

FORMAT = "[%(asctime)s][%(levelname)-5.5s] %(message)s"
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.INFO)

def get_all_sound_recordings():
    sound_recordings = get_all_sound_recordings()
    for record in sound_recordings:
        log.info('PRINTING RECORD:{}'.format(record.id))

def main():
    fire.Fire()

main()
