# Imports
from pytube import YouTube
from pytube import Playlist
import os

# Taking link of playlist
link = input('Digite o link da playlist: ')

# Oppening the playlist and splitting all videos
playlist = Playlist(link)

# Print the title of playlist

print(f"Playlist: {playlist.title}")

# This variable is a counter for print how many was downloaded
counter = 0

# Taking url by url and downloading them
for url in playlist.video_urls:
    counter +=1
    print(f"Downloading ({counter}/{len(playlist)})")
    ys = YouTube(url)
    print(f'Title: {ys.title}')

    # Getting audio only
    v = ys.streams.get_audio_only()

    # Transwindowing the mp4 for mp3 and saving in the path 'musics'
    out_file = v.download(output_path="musics")
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    os.system('cls')