##
# mpy3.py
# A tkinter program to download songs

# For GUI
import tkinter as tk
import tkinter.scrolledtext as scrolledtext

# For the actual download
import youtube_dl

# For getting home path
from pathlib import Path

###########
# GLOBALS #
###########
# TODO: Add check this exists and such
DL_DIR = f"{Path.home()}\\Music\\MPy3\\"

# TODO: Be able to pick file format, see resulting file size
# TODO: AtomicParsley for metadata

# MAYBE: Select file format
# They are downloaded to f"{Path.home()}\\Music\\MPy3\\"
# MAYBE: Pop up new window showing which ones are being downloaded
# Say ok! Give button to open folder?


def download(songs_str: str):
    
    """
    Download a list of songs separated by new lines using youtube-dl as mp3s
    """
    # Options from https://github.com/ytdl-org/youtube-dl/blob/master/README.md#embedding-youtube-dl
    ytdl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{DL_DIR}\\%(title)s.%(ext)s',
        'add-metadata': True,
        'embed-thumbnail': True
        
    }
    
    songs = songs_str.split('\n')
    with youtube_dl.YoutubeDL(ytdl_opts) as ytdl:
        for song in songs:
            # Skip empty lines
            if not song:
                continue

            print("Downloading", song)
            ytdl.download([song])


def download_wrapper(txt_area):
    # Get text from line 1, column 0 to end
    download(txt_area.get("1.0", tk.END))

    # Clear it
    txt_area.delete("1.0", tk.END)
    
# Text box where you paste links, separated by new lines
def main():
    """
    For setting up tkinter
    """
    root = tk.Tk()
    root.title("MPy3")
    root.geometry("300x200")

    # Text entry
    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD,
                                      width=40, height=8,)
    text_area.pack()

    # Download button, use lambda to pass arguments
    button = tk.Button(root, text="Download", command=lambda: download_wrapper(text_area))
    button.pack()

    # Let it be
    text_area.focus()
    root.mainloop()




if __name__ == "__main__":
    main()

