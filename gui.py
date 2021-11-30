# Imports
from PySimpleGUI.PySimpleGUI import WIN_CLOSED
from pytube import YouTube
from pytube import Playlist
import os
import PySimpleGUI as sg    

class GUI():
    # Theme
    sg.theme('darkpurple4')
    
    def __init__(self):  
        # Set colum 
        colum = [[sg.Text('', size=(45, 4), key='input', font=('ANY 2', 15), background_color='purple', text_color='pink1')],
                [sg.Text('Enter the link here:'), sg.InputText(size=(30, 1), font=('ANY 2', 11)), sg.Button(button_text='Download', size=(50, 1), button_color='purple', border_width=0, font=('Helvetica', 12))],   
        ]
        # Set layout
        layout = [
            [sg.Column(colum, vertical_alignment='center', justification='center')]
        ]

        # Set GUI
        self.window = sg.Window('Downloader of playlists', size=[500, 150])

        # Put layout
        self.window.Layout(layout)


        # Loop
        while True:

            button, self.value = self.window.Read() # Call GUI
            # Press Button
            if button == 'Download':
                # Check link
                if self.value[0].count('https') == 0 or self.value[0].count('playlist') == 0:
                    self.update("wait...\nwhere's the link of the playlist?")
                    
                else:
                    self.update('starting...')
                    link = self.value[0]

                    # Open the playlist and split all videos
                    self.playlist = Playlist(link)

                    # Print the title of playlist
                    self.update(f"Playlist: {self.playlist.title}")

                    # This variable is a counter for print how many was downloaded
                    counter = 0

                    # Take url by url and downloading them
                    for url in self.playlist.video_urls:
                        counter +=1
                        ys = YouTube(url)
                        self.update(f"Downloading ({counter}/{len(self.playlist)})"
                                    f'\nTitle: {ys.title}'
                        
                        )

                        # 'try' for if have a chance from music already downloaded
                        try:
                            # Getting audio only
                            v = ys.streams.get_audio_only()

                            self.check_path(ys.title)
                            # Transform the mp4 for mp3 and saving in the path 'musics'
                            out_file = v.download(output_path=f"musics")
                            base, ext = os.path.splitext(out_file)
                            new_file = base + '.mp3'
                            os.rename(out_file, new_file)
                            os.system('cls') 
                        except (FileExistsError):
                            self.update(f'You already download:\n{ys.title}')

                    self.update('Sucessful download.')

            elif button == WIN_CLOSED: # Break
                break
        
        # Close aplicattion
        self.window.close()

    # Check if already have the path of the music.
    def check_path(self, archiver_path):
        try:
            with open(f'musics\\{archiver_path}.mp3') as msc:
                raise(FileExistsError) # Raise FileExistsError for pass this download
        
        # If don't have, don't raise error
        except FileNotFoundError:
            pass

    # Update the print of GUI
    def update(self, text):
        self.window.find_element('input').Update(text)
        self.window.refresh()
    
        
# Initialize
app = GUI()