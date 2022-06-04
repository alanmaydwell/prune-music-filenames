# Prune Music Filenames
Remove band and album names from music filenames within a directory that are in the format supplied by Bandcamp (band-album-track number-song name) and save a new copy of each with just track number and song name.    

e.g. copy "band-album-01-song.ogg" as "01-song.ogg"

## Requires
Python 3. Only uses standard library.

## How to use
- Copy `prune_music_filenames.py` to the album directory and execute it there.
- Will automatically process any files with extensions "aac", "alac", "aiff", "flac", "mp3", "m4a", "ogg", and "wav"
- If digit found in file, will save a new copy of the file with filename starting from the digit. Will not save anything if no digit found.
- Does not make any changes to the original files that meet the criteria (has the right sort of extension and contains a digit). **However, will overwrite any files that already have the related destination filename, so take care if you want to preserve these.**
- Note if the original filenames contain other digits, such as in the album name (e.g. 1812 Overture), these can be catered for by setting the skip_digits parameter in the script.
