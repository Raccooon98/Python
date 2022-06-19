from tkinter import *
import capture
import note
root = Tk()
root.title("캡쳐&메모!")
root.geometry("330x165")
root.resizable(False,False)
def stop():
    root.destroy()
btn_capture = Button(root,width=20,height=5, text="캡쳐",command=capture.capture)
btn_capture.grid(row=0,column=0,sticky="w")
btn_memo = Button(root,width=20,height=5, text="메모", command=note.open_image)
btn_memo.grid(row=0,column=0,sticky="e")
btn_quit = Button(root,width=40,height=2, text="종료",command=stop)
btn_quit.grid(row=1, column=0, sticky="w")

root.mainloop() 
