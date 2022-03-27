from tkinter import *
import urllib.request


root = Tk()
root.title("Resim indirici")
root.geometry("300x300+700+250")
root.resizable(width=False, height=False)
backgroundColor = Label(bg="#2F4F4F", width=300, height=300)
backgroundColor.place(x=0, y=0)
root.iconbitmap("image.ico")


def indir():
    url = entry1.get()
    urllib.request.urlretrieve(url, "resim.jpg")


label1 = Label(text="URL GİRİNİZ :", font="Oswald 14", bg="#2F4F4F", fg="white")
label1.place(x=2, y=10)

entry1 = Entry(bg="lightgray", width=45)
entry1.place(x=2, y=40)
entry1.focus()

buton1 = Button(text="İndir", command=indir)
buton1.place(x=240, y=70)

# Örnek fotoğraf linki : https://wallpaper.dog/large/5448919.jpg


root.mainloop()
