pip install pytube
from tkinter import *
from pytube import YouTube as YT
window  = Tk()
window.title("2k19 youtube video download")
Label(window, text = "Youtube downloader", font = 'arial 20 bold').pack()
link = StringVar()
Label(window, text = "Paste your link", font = 'arial 20 bold').pack()
linkEntry = Entry(window, width = 80, textvariable = link.pack())
def Download():
  url = YT(str(link.get()))
  format = url.streams.filter(progressive = True, file_extension = "mp4")
  video = format.first()
  video = Download()
Button(window, text = "Download", font = 'arial 20 bold', bg = "yellow", command=Download).pack()
window.mainloop()

