from tkinter import *
import os
import win32com.client as win32
import win32gui
from tkinter.filedialog import *
from PIL import Image
def open_image():
    global name
    name = askopenfilename(title = "이미지 선택", filetypes = (("이미지 파일", "*.png"),("모든 파일", "*.*")))
    note()
def note():
    es = ""

    def newFile():
        top.title("제목없음- 메모장")
        file = None 
        ta.delete(1.0,END)

    def openImage():
        name = askopenfilename(title = "이미지 선택", filetypes = (("이미지 파일", "*.png"),("모든 파일", "*.*")))
        image = PhotoImage(file = name,master=top)
        label = Label(top, image = image)
        label.pack()


    def openFile():
        file = askopenfilename(title = "파일 선택", filetypes = (("텍스트 파일", "*.txt"),("모든 파일", "*.*")))
        top.title(os.path.basename(file) + " - 메모장")
        ta.delete(1.0, END)
        f = open(file,"r", encoding='UTF8')
        ta.insert(1.0,f.read())
        f.close()

    def saveFile():
        hwp = win32.Dispatch('HWPFrame.HwpObject')
        hwp.XHwpWindows.Item(0).Visible = True
        hwp.InsertPicture(name, Embedded=True, sizeoption=0)  
        hwp.Run("MoveDocEnd")
        hwp.Run("BreakPara") 
        def write(s):
            act=hwp.CreateAction("InsertText")
            set=act.CreateSet()
            act.GetDefault(set)
            set.SetItem("Text",s)
            ret=act.Execute(set)
        files = [('한글파일', '*.hwp'),
            ('모든 파일', '*.*')]
        ts = str(ta.get(1.0, END))
        write(ts)  

    



    def cut():
        global es
        es = ta.get(SEL_FIRST, SEL_LAST)
        ta.delete(SEL_FIRST, SEL_LAST)

    def copy():
        global es
        es = ta.get(SEL_FIRST, SEL_LAST)

    def paste():
        global es
        ta.insert(INSERT, es)

    def delete():
        ta.delete(SEL_FIRST, SEL_LAST)

    def help():
        he = Toplevel(top)
        he.geometry("200x200")
        he.title("정보")
        lb = Label(he, text = "메모장 버전 1.0\n 파이썬으로 만든 메모장입니다^^")
        lb.pack()

    top = Tk()
    top.title("메모장")
    top.geometry("800x600")

    # frame1= Frame(top,relief="solid",border=1)
    # frame1.pack(side="top",fill="both",expand=True)
    image = PhotoImage(file = name,master=top)
    label = Label(top, image = image)
    label.pack()

    frame2= Frame(top,relief="solid",border=1)
    frame2.pack(side="bottom",fill="both",expand=True)

    ta = Text(frame2)
    sb = Scrollbar(ta)
    sb.config(command = ta.yview)
    top.grid_rowconfigure(0, weight=1)
    top.grid_columnconfigure(0, weight=1)
    sb.pack(side = RIGHT, fill = Y)
    ta.pack(expand=True,fill="both")

    file = None


    mb = Menu(top)
    fi = Menu(mb, tearoff=0)
    fi.add_command(label="새파일", command=newFile)
    fi.add_command(label="이미지",command=openImage)
    fi.add_command(label="열기", command=openFile)
    fi.add_command(label="저장", command=saveFile)
    fi.add_separator()
    fi.add_command(label="종료", command=top.destroy)
    mb.add_cascade(label="파일", menu=fi)

    e = Menu(mb, tearoff=0)
    e.add_command(label="잘라내기", command=cut)
    e.add_command(label="복사", command=copy)
    e.add_command(label="붙이기", command=paste)
    e.add_command(label="삭제", command=delete)
    mb.add_cascade(label="편집", menu=e)

    h = Menu(mb, tearoff=0)
    h.add_command(label="메모장 정보", command = help)
    mb.add_cascade(label="도움말", menu=h)

    top.config(menu=mb)

    top.mainloop()