import logging
import csv
import fire

from data.logic import get_all_sound_recordings

FORMAT = "[%(asctime)s][%(levelname)-5.5s] %(message)s"
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)


def get_all_from_db():
    sound_recordings = get_all_sound_recordings()
    for record in sound_recordings:
        log.info('PRINTING RECORD:{}'.format(record.id))


def parse_file_from_cli(file_path):
    with open(file_path, 'r') as f:
        input_records = csv.DictReader(f, delimiter=',')
        for input_record in input_records:
            log.debug('ROW FROM FILE {}'.format(input_record['artist']))


def main():
    fire.Fire()


main()
