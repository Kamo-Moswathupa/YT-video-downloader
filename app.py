from os import link
from turtle import right, title
from pytube import YouTube
from tkinter import *

def download():
    link = entry.get()
    yt = YouTube(link)
    yd = yt.streams.get_highest_resolution()
    yd.download('./')
    

def chek_link():
    link = entry.get()
    yt = YouTube(link)
    label.config(text=yt.title , font=('Ink Free', 15))
    
    

window = Tk()
window.title('Video Downloader')
window.geometry('660x420')
window.resizable(0,0)
window.config(bg='#333036')

button = Button(window, text='Download', command=download)
button.place(height= 40,width= 100, x=500, y=100)
button.config(bg='#333036', fg='#ffffff', font=10)

button = Button(window, text='Check Link', command=chek_link)
button.place(height= 40,width= 100, x=380, y=100)
button.config(bg='#333036', fg='#ffffff', font=10)

entry = Entry()
entry.pack(pady= 20)
entry.config(width=30)
entry.config(font=('Ink Free', 20))
entry.config(bg='#333036', fg='#299306')

label = Label(window)
label.place( x=30, y=200)
label.config(bg='#333036', fg='#299306')


window.mainloop()