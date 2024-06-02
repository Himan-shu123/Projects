from tkinter import Tk, Label, Entry, Button, StringVar,Radiobutton
from pytube import YouTube

def download_video():
    link = link_entry.get()
    choice = choice_var.get()
    if choice == "Video":
        youtube = YouTube(link)
        videos = youtube.streams.filter(progressive=True)
        print("Available video streams:")
        for i, video in enumerate(videos):
            print(f"{i}: {video}")
        stream_index = int(stream_entry.get())
        videos[stream_index].download()
        print("Video downloaded successfully!")
    elif choice == "Audio":
        youtube = YouTube(link)
        audio = youtube.streams.filter(only_audio=True)
        print("Available audio streams:")
        for i, aud in enumerate(audio):
            print(f"{i}: {aud}")
        stream_index = int(stream_entry.get())
        audio[stream_index].download()
        print("Audio downloaded successfully!")

# Create main window
root = Tk()
root.title("YouTube Downloader")

# Label for YouTube link
link_label = Label(root, text="Enter YouTube link:")
link_label.grid(row=0, column=0)

# Entry for YouTube link
link_entry = Entry(root, width=50)
link_entry.grid(row=0, column=1)

# Label for choice
choice_label = Label(root, text="Choose download type:")
choice_label.grid(row=1, column=0)

# Radio button for video or audio
choice_var = StringVar()
choice_var.set("Video")
video_radio = Radiobutton(root, text="Video", variable=choice_var, value="Video")
video_radio.grid(row=1, column=1)
audio_radio = Radiobutton(root, text="Audio", variable=choice_var, value="Audio")
audio_radio.grid(row=1, column=2)

# Label for stream selection
stream_label = Label(root, text="Enter stream index:")
stream_label.grid(row=2, column=0)

# Entry for stream selection
stream_entry = Entry(root, width=10)
stream_entry.grid(row=2, column=1)

# Button to initiate download
download_button = Button(root, text="Download", command=download_video)
download_button.grid(row=3, column=0, columnspan=2)

# Start GUI main loop
root.mainloop()
