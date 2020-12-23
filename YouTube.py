from tkinter import *
import os
from pytube import *
import pyperclip as pc
from tkinter import messagebox

window = Tk()

window.title("YouTube Downloader") # title of first window
window.configure(background='pink') # change pink for any colour. 

window.geometry('530x200') # resized.

get = print(os.getcwd()) # need this to show where the download has gone.

lbl = Label(window, text="YouTube Ripper", font=("Arial Bold", 50)) # window label and font.
lbl.configure(background="pink")

lbl.grid(column=0, row=0) 
lbl = Label(window, text="Paste the YouTube Link here", font=("Arial Bold", 20)) 
lbl.configure(background="pink")
lbl.grid(column=0, row=1) 
x = Entry(window,width=70) 
x.grid(column=0, row=3) 
x.focus()


def clicked():
    try:
        x_data = x.get()
        link = x_data
        yt = YouTube(link)
        ys = yt.streams.get_highest_resolution() # automatically downloading highest quality stream
        ys.download() # downloading
        messagebox.showinfo("Success!", "file downloaded to " + os.getcwd()) # once downloaded report back with filepath
    except:
        messagebox.showinfo("WHOOOPS!","Check the URL and try again.") # if failed
        
def paste():
    try:
        x.focus() # cursor locks to paste window auto
        x.event_generate('<Control-v>') # replicate ctrl v as a button comman
    except:
        messagebox.showinfo("Failed","Nothing to paste maybe? I dunno.")
        

btn = Button(window, text="Download", bg="black", fg="white",command=clicked) # button colours
btn2 = Button(window, text="Paste From Clipboard", bg="green", fg="white",command=paste) 


btn.grid(column=0, row=7) 
lblblank = Label(window, text=" ", font=("Arial Bold", 20)) 
btn2.grid(column=0, row=6)


window.mainloop()
