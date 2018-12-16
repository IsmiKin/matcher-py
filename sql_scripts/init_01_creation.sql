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
