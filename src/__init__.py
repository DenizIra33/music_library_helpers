import os
import shutil
from pathlib import Path

class MP3Converter():
    def __init__(self, path, ext, dirName, delete = True):
        """Class that takes folder of music files of one file type, 
        converts them to mp3 and creates a new directory and moves them into it
        Input path of files that you would like to convert
        Extension of files you would like to convert i.e. WAV
        Folder name of the new directory you would like to create"""
        self.path = path
        self.ext = ext
        self.dirName = dirName
        self.delete = delete

    def escape_quotes(self, path):
        return path.replace("'", "\'")

    def mp3(self):
        """
        Converts all files in path with entered extension to mp3
        """
        filepath = self.escape_quotes(str(self.path))
        file_path_without_extension = self.escape_quotes(filepath.strip(self.ext))
        print(filepath) 
        os.system('ffmpeg -i "{}" -y -ar 44100 -ac 2 -b:a 320k "{}.mp3"'.format(filepath, file_path_without_extension))

    def delete_wav_files(self):
        filepath = str(self.path)
        os.system("rm -rf '{}'".format(self.escape_quotes(filepath)))

    def execute(self):
        self.mp3()
        if self.delete:
            self.delete_wav_files()

    def make_dir(self):
        """
        Creates a directory for mp3's and moves all 
        previously created mp3's into it and moves the directory up one
        """
        mp3_directory = self.path + "/" + self.dirName
        if not os.path.exists(mp3_directory):
            os.makedirs(mp3_directory)
        for filename in os.listdir(self.path):
            if (filename.endswith(".mp3")):
                source = os.path.join(self.path, filename)
                dest = shutil.move(source, mp3_directory)
                print(f"Moved {filename} to {dest}")
        try:
            parent_dir = Path(mp3_directory).parents[1]
            shutil.move(mp3_directory, parent_dir)
        except IndexError:
            # no upper directory
            pass

