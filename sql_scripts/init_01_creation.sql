CREATE TABLE "sound_recordings" (
  "id" SERIAL PRIMARY KEY,
  "artist" text NOT NULL,
  "title" text NOT NULL,
  "isrc" text NULL,
  "duration" int NULL
);
