#!/usr/bin/env python3

import os
import shutil


class BandcampFilenamePrune:
    """Remove band and album names from music filenames in a directory, and
    save new copy of each file with just track number and name. Created
    to process files downloaded from Bandcamp.
    
    e.g. copy "band-album-01-song.ogg" as "01-song.ogg"
    
    
    Find all files with particular audio file extensions in same dir
    ("aac", "alac", "aiff", "flac", "mp3", "m4a", "ogg", "wav").
    Look for position of digit in each filename. If digit found, make
    a new copy of the file with new filename starting from the digit.
    Can optionally skip a number of digits to cater for album names
    that have digits within them. 
      
    Parameters:
        file_path - optional path to directory with the files, defaults to
                    current working directory
        skip_digits - optional number of digits to skip.
    """
    def __init__(self, file_path=None, skip_digits=0):
        if not file_path:
            self.dir = os.getcwd()
        else:
            self.dir = file_path
        self.skip_digits = skip_digits
        self.valid_extensions = ["aac", "alac", "aiff", "flac", "mp3", "m4a", "ogg", "wav"]
        
        filenames = self.get_music_filenames()
        for filename in filenames:
            wanted = find_wanted_filename(filename, self.skip_digits)
            if filename != wanted:
                print(filename, "->", wanted)
                self.copy_file(filename, wanted)

    def get_music_filenames(self):
        filenames = os.listdir(self.dir)
        return [f for f in filenames
                if f.split(".")[-1].lower() in self.valid_extensions]

    def copy_file(self, original, new):
        source = os.path.join(self.dir, original)
        destination = os.path.join(self.dir, new)
        shutil.copy(source, destination)


def find_wanted_filename(filename, skip_digits=0):
    """Look for digit in string, if found, return the part of the string
    from the digit onwards, otherwise return the original string.
    Also option to ignore number of digits, so can be part of string from
    nth digit.
    
    Args:
        filename - the string to be processed
        skip_digits (int) - optional number of digits to skip
    """
    wanted = filename
    for i, c in enumerate(filename):
        if c.isdigit():
            if skip_digits < 1:
                wanted = filename[i:]
                break
            else:
                skip_digits -= 1
    return wanted


if __name__ == "__main__":
    go = BandcampFilenamePrune(skip_digits=0)
