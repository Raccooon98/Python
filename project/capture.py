from tkinter import *
from PIL import Image,ImageGrab
import os
from cv2 import destroyWindow
import mouse, pyautogui
def capture():
    global ROI_SET, x1, y1, x2, y2, file
    ROI_SET = False

    def file_name():
        global file
        file=entry.get()
        set_roi()
        
    def set_roi():
        print("Select your ROI using mouse drag.")
        while(mouse.is_pressed() == False):
            x1, y1 = mouse.get_position()
            while(mouse.is_pressed() == True):
                x2, y2 = mouse.get_position()
                while(mouse.is_pressed() == False):
                    print("Your ROI : {0}, {1}, {2}, {3}".format(x1, y1, x2, y2))
                    ROI_SET = True
                    print(ROI_SET)   
                    if ROI_SET == True:
                        pyautogui.screenshot(f'C:/Users/junbs/OneDrive/바탕 화면/깃허브/Python/project/{file}.png',region=(x1,y1,x2-x1,y2-y1))
                        print("done.")
                        cp.destroy()
                        image=Image.open(f'C:/Users/junbs/OneDrive/바탕 화면/깃허브/Python/project/{file}.png')
                        resize_image = image.resize((400,280))
                        resize_image.save(f'C:/Users/junbs/OneDrive/바탕 화면/깃허브/Python/project/{file}.png', "png", quality=95)
                        image.show()
                    return
    cp=Tk()
    cp.title("캡쳐도구")
    cp.geometry("400x200")
    cp.resizable(False,False)
    a = Label(cp,text="파일 이름 작성")
    a.pack(side="top")
    entry = Entry(cp,width=40)
    entry.pack(side="left")
    rb=Button(cp,text="입력", command=file_name,width=5)
    rb.pack(side="right")
    cp.mainloop()
