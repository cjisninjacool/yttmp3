from tkinter import *
from tkinter import filedialog
from pytube import YouTube
root = Tk()

def getfolder():
    root.filename = filedialog.askdirectory(initialdir="/")
    folder = root.filename
    return folder

def saveyoutube(link,saveplace,labeldone,labeldtwo):
    yt = YouTube(link)
    tex = "Title: ", yt.title
    texe = "Views: ", yt.views
    labeldone.config(text = tex)
    labeldtwo.config(text = texe)
    yd = yt.streams.get_highest_resolution()
    yd.download(saveplace)


e = Entry(root)

labelone = Label(root,text = "")
labeltwo = Label(root)

done = Button(root,text= "Done",command= lambda: saveyoutube(e.get(),getfolder(),labelone,labeltwo))
done.pack()
labelone.pack()
labeltwo.pack()
e.pack()
root.mainloop()
