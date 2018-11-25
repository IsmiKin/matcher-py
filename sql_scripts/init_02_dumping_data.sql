COPY sound_recordings
(artist, title, isrc, duration)
FROM '/docker-entrypoint-initdb.d/initial_sample_data.csv'
DELIMITER ','
CSV HEADER;
