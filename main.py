# coding = UTF-8
import search, sys
from tkinter import *
from getpass import getuser
from tkinter import ttk
from os import path
from os import system
from tkinter.messagebox import *

UserName = getuser()
WorkDir = path.dirname(__file__)
Name = Artist = ""
Id = Id1 = Id2 = Id3 = Id4 = Id5 = 0
Nm1 = Nm2 = Nm3 = Nm4 = Nm5 = ""
Art1 = Art2 = Art3 = Art4 = Art5 = ""

def Initialize():
    global Id1, Id2, Id3, Id4, Id5
    Id = Id1 = Id2 = Id3 = Id4 = Id5 = 0
    Nm1.set(" 空 "); Nm2.set(" 空 "); Nm3.set(" 空 "); Nm4.set(" 空 "); Nm5.set(" 空 ")
    Art1.set(" 空 "); Art2.set(" 空 "); Art3.set(" 空 "); Art4.set(" 空 "); Art5.set(" 空 ")

def Download(ID, SongName):
    temp = "http://music.163.com/song/media/outer/url?id=" + str(ID) + ".mp3"
    system("aria2c -s 5 -x 5 -j 10 -d C:\\Users\\" + UserName + "\\Downloads\\MusicDownload "  + "-o " + SongName + ".mp3 " + temp)
    system("start C:\\Users\\" + UserName + "\\Downloads")
    showinfo("提示", "下载完成，歌曲保存在下载目录！")

def Down1():
    Download(Id1, Nm1.get())

def Down2():
    Download(Id2, Nm2.get())

def Down3():
    Download(Id3, Nm3.get())

def Down4():
    Download(Id4, Nm4.get())

def Down5():
    Download(Id5, Nm5.get())

def Fun(idpos, artpos, List):
    global Id, Name, Artist
    i = idpos + 5
    Id = 0
    while (str.isdigit(List[i])):
        Id = Id * 10 + int(List[i])
        i += 1
    i += 9
    Name = ""
    while (List[i] != "\"" or List[i - 1] == "\\"):
        Name += List[i]
        i += 1
    i = artpos
    while (List[i] != ","):
        i = i + 1
    i += 9
    Artist = ""
    while (List[i] != "\"" or List[i - 1] == "\\"):
        Artist += List[i]
        i += 1

def Parse(List):
    cnt = 0
    pos1 = pos2 = pos3 = pos4 = pos5 = -1
    art1 = art2 = art3 = art4 = art5 = -1
    Size = len(List)
    for i in range(Size - 4):
        print(List[i], end = "")
        if List[i] == "\"" and List[i + 1] == "i" and List[i + 2] == "d" and List[i + 3] == "\"" :
            cnt = cnt + 1
            if cnt % 4 == 1 :
                if pos1 == -1 : pos1 = i; continue
                if pos2 == -1 : pos2 = i; continue
                if pos3 == -1 : pos3 = i; continue
                if pos4 == -1 : pos4 = i; continue
                if pos5 == -1 : pos5 = i; continue
            elif cnt % 4 == 2:
                if art1 == -1 : art1 = i; continue
                if art2 == -1 : art2 = i; continue
                if art3 == -1 : art3 = i; continue
                if art4 == -1 : art4 = i; continue
                if art5 == -1 : art5 = i; continue
    print("\n", pos1, pos2, pos3, pos4, pos5)
    print("\n", art1, art2, art3, art4, art5)
    global Id1, Id2, Id3, Id4, Id5
    global Nm1, Nm2, Nm3, Nm4, Nm5
    global Art1, Art2, Art3, Art4, Art5
    Initialize()
    Fun(pos1, art1, List)
    Id1 = Id
    Nm1.set(Name)
    Art1.set(Artist)
    Fun(pos2, art2, List)
    Id2 = Id
    Nm2.set(Name)
    Art2.set(Artist)
    Fun(pos3, art3, List)
    Id3 = Id
    Nm3.set(Name)
    Art3.set(Artist)
    Fun(pos4, art4, List)
    Id4 = Id
    Nm4.set(Name)
    Art4.set(Artist)
    Fun(pos5, art5, List)
    Id5 = Id
    Nm5.set(Name)
    Art5.set(Artist)
def Search():
    Name = entry.get()
    search.Download(Name)
    with open("Tmp.html", encoding = "utf-8") as f:
        Tmp = f.read()
        f.close()
    Parse(Tmp)

def No_x():
    Label(window, text = "序号", font = ("微软雅黑", 12)).place(x = 75, y = 125, anchor = "center")
    Label(window, text = " 1 ", font = ("微软雅黑", 11)).place(x = 75, y = 160, anchor = "center")
    Label(window, text = " 2 ", font = ("微软雅黑", 11)).place(x = 75, y = 195, anchor = "center")
    Label(window, text = " 3 ", font = ("微软雅黑", 11)).place(x = 75, y = 230, anchor = "center")
    Label(window, text = " 4 ", font = ("微软雅黑", 11)).place(x = 75, y = 265, anchor = "center")
    Label(window, text = " 5 ", font = ("微软雅黑", 11)).place(x = 75, y = 300, anchor = "center")

def Nm_x():
    Label(window, font = ("微软雅黑", 12), text = " 歌曲名 ").place(x = 215, y = 125, anchor = "center")
    Label(window, font = ("微软雅黑", 10), textvariable = Nm1).place(x = 215, y = 160, anchor = "center")
    Label(window, font = ("微软雅黑", 10), textvariable = Nm2).place(x = 215, y = 195, anchor = "center")
    Label(window, font = ("微软雅黑", 10), textvariable = Nm3).place(x = 215, y = 230, anchor = "center")
    Label(window, font = ("微软雅黑", 10), textvariable = Nm4).place(x = 215, y = 265, anchor = "center")
    Label(window, font = ("微软雅黑", 10), textvariable = Nm5).place(x = 215, y = 300, anchor = "center")

def Art_x():
    Label(window, font = ("微软雅黑", 12), text = " 歌手名 ").place(x = 380, y = 125, anchor = "center")
    Label(window, font = ("微软雅黑", 10), textvariable = Art1).place(x = 380, y = 160, anchor = "center")
    Label(window, font = ("微软雅黑", 10), textvariable = Art2).place(x = 380, y = 195, anchor = "center")
    Label(window, font = ("微软雅黑", 10), textvariable = Art3).place(x = 380, y = 230, anchor = "center")
    Label(window, font = ("微软雅黑", 10), textvariable = Art4).place(x = 380, y = 265, anchor = "center")
    Label(window, font = ("微软雅黑", 10), textvariable = Art5).place(x = 380, y = 300, anchor = "center")

def Down_x():
    Label(window, font = ("微软雅黑", 12), text = " 下载 ").place(x = 500, y = 125, anchor = "center")
    ttk.Button(window, text = '下载', command = Down1).place(x = 500, y = 160, anchor = "center")
    ttk.Button(window, text = '下载', command = Down2).place(x = 500, y = 195, anchor = "center")
    ttk.Button(window, text = '下载', command = Down3).place(x = 500, y = 230, anchor = "center")
    ttk.Button(window, text = '下载', command = Down4).place(x = 500, y = 265, anchor = "center")
    ttk.Button(window, text = '下载', command = Down5).place(x = 500, y = 300, anchor = "center")

def main():
    global Nm1, Nm2, Nm3, Nm4, Nm5
    global Art1, Art2, Art3, Art4, Art5
    global window, entry
    window = Tk()
    window.title("网易云音乐下载器 2.0  Powered by 印皓显")
    window.geometry("600x350")
    window.iconphoto(False, PhotoImage(file = WorkDir + "\\ICON.png"))
    lb = Label(window, text = "网易云音乐下载器", width = 16, height = 1, justify = "center", anchor = "nw", font = ("宋体", 18), fg = "white", bg = "grey", padx = 10, pady = 5)
    lb.place(x = 300, y = 35, anchor = "center")
    Nm1  = StringVar(); Nm2 = StringVar(); Nm3 = StringVar(); Nm4 = StringVar(); Nm5 = StringVar()
    Art1  = StringVar(); Art2 = StringVar(); Art3 = StringVar(); Art4 = StringVar(); Art5 = StringVar()
    Initialize()
    sv1 = StringVar()
    sv1.set("在这里输入要搜索的歌名")
    entry = ttk.Entry(window, width = 40, justify = CENTER, font = ("微软雅黑", 10),  exportselection = 0, textvariable = sv1)
    entry.place(x = 55, y = 72.5)
    png = PhotoImage(file =  WorkDir + "\\Search.png")
    button_search = ttk.Button(window, image = png, command = Search)
    button_search.place(x = 450, y = 68)
    No_x(); Nm_x(); Art_x(); Down_x()
    window.mainloop()

if __name__ == "__main__":
    main()