# Helpers to convert files to MP3 320kbps and flatten Soulseek Directory structure


How to use:
1. Fork the library.
2. Install ```ffmpeg```. See [here](https://ffmpeg.org/download.html) for installation details.
3. To flatten file hierarchy, execute the notebook ```flatten_and_copy_files.py```. Make sure to change ```DISCOGS_DATA_DIR``` and ```DESTINATION_DIR``` according to your needs.
4. To convert files, execute ```convert_file_to_mp3.ipynb```. Make sure to change ```DIR``` according to your file hierarchy.