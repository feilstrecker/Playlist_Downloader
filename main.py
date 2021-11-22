from pytube import YouTube
from pytube import Playlist
import os

link = input('Digite o link da playlist: ')


playlist = Playlist(link)
print(f"Playlist: {playlist.title}")
for url in playlist.video_urls:
    ys = YouTube(url)
    print(f'Titulo: {ys.title}')
    v = ys.streams.get_audio_only()
    out_file = v.download()
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)