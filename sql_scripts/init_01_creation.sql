CREATE TABLE "sound_recordings" (
  "id" SERIAL PRIMARY KEY,
  "artist" text NOT NULL,
  "title" text NOT NULL,
  "isrc" text NULL,
  "duration" int NULL
);

CREATE TABLE "files_processed" (
  "hash" text PRIMARY KEY,
  "filename" text NOT NULL,
  "file_time_update" timestamp NOT NULL
);

CREATE TABLE "sound_record_match" (
  "match_id" text  PRIMARY KEY,
  "row_number" integer NOT NULL,
  "artist" text NULL,
  "title" text NULL,
  "isrc" text NULL,
  "duration" integer NULL,
  "score" integer NOT NULL,
  "files_processed_FK" text NOT NULL,
  "sound_recordings_FK" int NOT NULL,
  FOREIGN KEY ("files_processed_FK") REFERENCES "files_processed" ("hash"),
  FOREIGN KEY ("sound_recordings_FK") REFERENCES "sound_recordings" ("id")
);
