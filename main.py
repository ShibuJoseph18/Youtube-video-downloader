from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    """It takes YouTube video url and system path in your local system and
    downloads the video to the specified path"""

    try:
        yt = YouTube(url)
        video_details = yt.streams.filter(progressive=True, file_extension="mp4")
        video_quality = video_details.get_highest_resolution()
        video_quality.download(output_path=save_path)
    except Exception as e:
        print(e)

def open_dialog():
    """It prompts the Tkinter desktop UI for choosing the system path"""

    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder:{folder}")
    return folder


if __name__ == "__main__":
    root = tk.Tk()

    video_url = input("Enter url: ")
    file_path = open_dialog()

    if file_path:
        print("File downloading...")
        download_video(url=video_url, save_path=file_path)
        print("File successfully downloaded :)")
    else:
        print("Invalid location")




