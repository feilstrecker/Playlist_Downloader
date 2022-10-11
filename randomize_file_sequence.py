from random import choice
import os

musics = os.listdir('musics\\')
c = 0

for i in range(len(musics)):
    old_name = choice(musics)
    new_name = f'{c} - {old_name}'
    os.rename(f'musics\\{old_name}', f'musics\\{new_name}')
    musics.remove(old_name)
    c += 1