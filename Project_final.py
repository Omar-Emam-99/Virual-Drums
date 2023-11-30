import tkinter as tk
from tkinter import * 
from tkinter.ttk import *
from tkinter import ttk
import pygame
import cv2
import numpy as np
import imutils
from collections import deque
import winsound 
from PIL import Image , ImageTk



splash_root = Tk()
splash_root.overrideredirect(True)

splash_width = 600 
splash_height = 310 

screen_width= splash_root.winfo_screenwidth()
screen_height= splash_root.winfo_screenheight()
x= (screen_width/2) - (splash_width/2)
y= (screen_height/2) - (splash_height/2)
splash_root.geometry(f'{splash_width}x{splash_height}+{int(x)}+{int(y)}')
bgr=PhotoImage(file="D://back//splash.png")
label_s = Label(splash_root,image=bgr)
label_s = Label( splash_root, image = bgr)
label_s.place(x = 0,y = 0)



def PlayWithCamera():
    

    lowblue = np.array([40,150,116])
    highblue = np.array([255,255,255]) 
    lowred = np.array([131,90,106])
    highred = np.array([255,255,255])
    
    #position_deques
    pts_blue = deque(maxlen=64)
    pts_red = deque(maxlen=64)
    
    
    #video capturing 
    cap = cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame,1)
        frame = imutils.resize(frame,height=700, width=900)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
      #blue_mask 
        mask_blue = cv2.inRange(hsv, lowblue, highblue)
        mask_blue = cv2.erode(mask_blue, None, iterations=2)
        mask_blue = cv2.dilate(mask_blue, None, iterations=2)
      #red_mask
        mask_red = cv2.inRange(hsv, lowred, highred)
        mask_red = cv2.erode(mask_red, None, iterations=2)
        mask_red = cv2.dilate(mask_red, None, iterations=2)
        
      #rectangles_drawing
      
        cv2.rectangle(frame, (0,188), (266,293), (0,255,0),2)
        cv2.putText(frame,'CRASH',(75 ,250),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)
        
        cv2.rectangle(frame, (634 ,188), (899 ,293), (0,255,0),2)
        cv2.putText(frame,'RIDE',(720 ,250),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)
    
        cv2.rectangle(frame, (0,388), (266,493), (0,255,0),2)
        cv2.putText(frame,'HIHAT',(75 ,450),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)
        
        cv2.rectangle(frame, (0 ,595), (266 ,699), (0,255,0),2)
        cv2.putText(frame,'SNARE',(75 ,650),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)
        
        cv2.rectangle(frame, (317,595), (583,699), (255,0,0),2)
        cv2.putText(frame,'BASS',(410 ,650),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)
        
        cv2.rectangle(frame, (634 ,595), (899 ,699), (0,255,0),2)
        cv2.putText(frame,'FLOOR',(720 ,650),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)
        
        cv2.rectangle(frame, (634,388), (899,493), (0,255,0),2)
        cv2.putText(frame,'TOM2',(720 ,450),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)
        
        cv2.rectangle(frame, (317 ,388), (583 ,493), (0,255,0),2)
        cv2.putText(frame,'TOM1',(410 ,450),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)
      #contour for blue 
        cnts = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        center = None
        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            if radius > 10:
                cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
                cv2.circle(frame, center, 5, (0, 0, 255), -1)
        pts_blue.appendleft(center)
        if pts_blue[0] != None and pts_blue[1] != None:
             if pts_blue[0][0] > 0 and pts_blue[0][1] > 188 and pts_blue[0][0] < 266 and pts_blue[0][1] < 293:
                    if pts_blue[1][0] > 0 and pts_blue[1][1] > 188 and pts_blue[1][0] < 266 and pts_blue[1][1] < 293:
                        pass
                    else:
                        winsound.PlaySound("D://SoundsSynthesis//CRASH.wav",winsound.SND_ASYNC)
                        
        if pts_blue[0] != None and pts_blue[1] != None:
             if pts_blue[0][0] > 634 and pts_blue[0][1] > 188 and pts_blue[0][0] < 899 and pts_blue[0][1] < 293:
                    if pts_blue[1][0] > 634 and pts_blue[1][1] > 188 and pts_blue[1][0] < 899 and pts_blue[1][1] < 293:
                        pass
                    else:
                        winsound.PlaySound("D://SoundsSynthesis//RIDE.wav",winsound.SND_ASYNC)               
        if pts_blue[0] != None and pts_blue[1] != None:
             if pts_blue[0][0] > 0 and pts_blue[0][1] > 388 and pts_blue[0][0] < 266 and pts_blue[0][1] < 493:
                    if pts_blue[1][0] > 0 and pts_blue[1][1] > 388 and pts_blue[1][0] < 266 and pts_blue[1][1] < 493:
                        pass
                    else:
                        winsound.PlaySound("D://SoundsSynthesis//HIHAT.wav",winsound.SND_ASYNC)
        if pts_blue[0] != None and pts_blue[1] != None:
             if pts_blue[0][0] > 0 and pts_blue[0][1] > 595 and pts_blue[0][0] < 266 and pts_blue[0][1] < 699:
                    if pts_blue[1][0] > 0 and pts_blue[1][1] > 595 and pts_blue[1][0] < 266 and pts_blue[1][1] < 699:
                        pass
                    else:
                        winsound.PlaySound("D://SoundsSynthesis//SNARE.wav",winsound.SND_ASYNC)                
        if pts_blue[0] != None and pts_blue[1] != None:
             if pts_blue[0][0] > 317 and pts_blue[0][1] > 595 and pts_blue[0][0] < 583 and pts_blue[0][1] < 699:
                    if pts_blue[1][0] > 317 and pts_blue[1][1] > 595 and pts_blue[1][0] < 583 and pts_blue[1][1] < 699:
                        pass
                    else:
                        winsound.PlaySound("D://SoundsSynthesis//BASS.wav",winsound.SND_ASYNC)                
        if pts_blue[0] != None and pts_blue[1] != None:
             if pts_blue[0][0] > 634 and pts_blue[0][1] > 595 and pts_blue[0][0] < 899 and pts_blue[0][1] < 699:
                    if pts_blue[1][0] > 634 and pts_blue[1][1] > 595 and pts_blue[1][0] < 899 and pts_blue[1][1] < 699:
                        pass
                    else:
                        winsound.PlaySound("D://SoundsSynthesis//FLOOR.wav",winsound.SND_ASYNC)                
        if pts_blue[0] != None and pts_blue[1] != None:
             if pts_blue[0][0] > 634 and pts_blue[0][1] > 388 and pts_blue[0][0] < 899 and pts_blue[0][1] < 493:
                    if pts_blue[1][0] > 634 and pts_blue[1][1] > 388 and pts_blue[1][0] < 899 and pts_blue[1][1] < 493:
                        pass
                    else:
                        winsound.PlaySound("D://SoundsSynthesis//TOM2.wav",winsound.SND_ASYNC)
        if pts_blue[0] != None and pts_blue[1] != None:
             if pts_blue[0][0] > 317 and pts_blue[0][1] > 388 and pts_blue[0][0] < 583 and pts_blue[0][1] < 493:
                    if pts_blue[1][0] > 317 and pts_blue[1][1] > 388 and pts_blue[1][0] < 583 and pts_blue[1][1] < 493:
                        pass
                    else:
                        winsound.PlaySound("D://SoundsSynthesis//TOM1.wav",winsound.SND_ASYNC)
                        
      #contour for red 
        cnts = cv2.findContours(mask_red, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        center = None
        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            if radius > 10:
                cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
                cv2.circle(frame, center, 5, (0, 0, 255), -1)
        pts_red.appendleft(center)
        
        if pts_red[0] != None and pts_red[1] != None:
             if pts_red[0][0] > 0 and pts_red[0][1] > 188 and pts_red[0][0] < 266 and pts_red[0][1] < 293:
                    if pts_red[1][0] > 0 and pts_red[1][1] > 188 and pts_red[1][0] < 266 and pts_red[1][1] < 293:
                        pass
                    else:
                        winsound.PlaySound("D://SoundsSynthesis//CRASH.wav",winsound.SND_ASYNC)
                        
        if pts_red[0] != None and pts_red[1] != None:
             if pts_red[0][0] > 634 and pts_red[0][1] > 188 and pts_red[0][0] < 899 and pts_red[0][1] < 293:
                    if pts_red[1][0] > 634 and pts_red[1][1] > 188 and pts_red[1][0] < 899 and pts_red[1][1] < 293:
                        pass
                    else:
                        winsound.PlaySound("D://SoundsSynthesis//RIDE.wav",winsound.SND_ASYNC)               
        if pts_red[0] != None and pts_red[1] != None:
             if pts_red[0][0] > 0 and pts_red[0][1] > 388 and pts_red[0][0] < 266 and pts_red[0][1] < 493:
                    if pts_red[1][0] > 0 and pts_red[1][1] > 388 and pts_red[1][0] < 266 and pts_red[1][1] < 493:
                        pass
                    else:
                        winsound.PlaySound("D://SoundsSynthesis//HIHAT.wav",winsound.SND_ASYNC)
        if pts_red[0] != None and pts_red[1] != None:
             if pts_red[0][0] > 0 and pts_red[0][1] > 595 and pts_red[0][0] < 266 and pts_red[0][1] < 699:
                    if pts_red[1][0] > 0 and pts_red[1][1] > 595 and pts_red[1][0] < 266 and pts_red[1][1] < 699:
                        pass
                    else:
                        winsound.PlaySound("D://SoundsSynthesis//SNARE.wav",winsound.SND_ASYNC)               
        if pts_red[0] != None and pts_red[1] != None:
             if pts_red[0][0] > 317 and pts_red[0][1] > 595 and pts_red[0][0] < 583 and pts_red[0][1] < 699:
                    if pts_red[1][0] > 317 and pts_red[1][1] > 595 and pts_red[1][0] < 583 and pts_red[1][1] < 699:
                        pass
                    else:
                        winsound.PlaySound("D://SoundsSynthesis//BASS.wav",winsound.SND_ASYNC)                
        if pts_red[0] != None and pts_red[1] != None:
             if pts_red[0][0] > 634 and pts_red[0][1] > 595 and pts_red[0][0] < 899 and pts_red[0][1] < 699:
                    if pts_red[1][0] > 634 and pts_red[1][1] > 595 and pts_red[1][0] < 899 and pts_red[1][1] < 699:
                        pass
                    else:
                        winsound.PlaySound("D://SoundsSynthesis//FLOOR.wav",winsound.SND_ASYNC)                
        if pts_red[0] != None and pts_red[1] != None:
             if pts_red[0][0] > 634 and pts_red[0][1] > 388 and pts_red[0][0] < 899 and pts_red[0][1] < 493:
                    if pts_red[1][0] > 634 and pts_red[1][1] > 388 and pts_red[1][0] < 899 and pts_red[1][1] < 493:
                        pass
                    else:
                        winsound.PlaySound("D://SoundsSynthesis//TOM2.wav",winsound.SND_ASYNC)
        if pts_red[0] != None and pts_red[1] != None:
             if pts_red[0][0] > 317 and pts_red[0][1] > 388 and pts_red[0][0] < 583 and pts_red[0][1] < 493:
                    if pts_red[1][0] > 317 and pts_red[1][1] > 388 and pts_red[1][0] < 583 and pts_red[1][1] < 493:
                        pass
                    else:
                        winsound.PlaySound("D://SoundsSynthesis//TOM1.wav",winsound.SND_ASYNC)
    
        cv2.imshow("frame", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break
    
    cap.release()
    cv2.destroyAllWindows()
        


def mainPage():
    splash_root.destroy()
    root = Tk()
    root.title('Virtual Drums App')
    
    root_width = 900 
    root_height = 700 

    screen_width= root.winfo_screenwidth()
    screen_height= root.winfo_screenheight()
    x= (screen_width/2) - (root_width/2)
    y= (screen_height/2) - (root_height/2)
    root.geometry(f'{root_width}x{root_height}+{int(x)}+{int(y)}')
    root.resizable(False,False)
    root.iconbitmap('D://back/icon.ico')
    bg = PhotoImage( file = "D://back//background2.png")
    label1 = Label(root, image = bg)
    label1.place(x = 0,y = 0)

    
    
    def Rudiments():
        master = Toplevel(root)
        master.title("RUDIMENTS PRACTICES")
        master_width = 900 
        master_height = 700 
        
        screen_width= master.winfo_screenwidth()
        screen_height= master.winfo_screenheight()
        x= (screen_width/2) - (master_width/2)
        y= (screen_height/2) - (master_height/2)
        master.geometry(f'{master_width}x{master_height}+{int(x)}+{int(y)}')
        master.resizable(False, False)
        master.iconbitmap('D://back/icon.ico')
        bg = PhotoImage( file = "D://back//background2.png")
        label1 = Label( master, image = bg)
        label1.place(x = 0,y = 0)
        pygame.mixer.init() 
        
        def play1(): 
            pygame.mixer.music.load("D://rudiments//Single_Stroke_Roll.mp3")
            pygame.mixer.music.play(loops=0)
        def play2(): 
            pygame.mixer.music.load("D://rudiments//Single_Stroke_4.mp3")
            pygame.mixer.music.play(loops=0)
        def play3(): 
            pygame.mixer.music.load("D://rudiments//Single_Stroke_7.mp3")
            pygame.mixer.music.play(loops=0)
        def play4(): 
            pygame.mixer.music.load("D://rudiments//Multiple_Bounce_Roll.mp3")
            pygame.mixer.music.play(loops=0)
        def play5(): 
            pygame.mixer.music.load("D://rudiments//Triple_Stroke_Roll.mp3")
            pygame.mixer.music.play(loops=0)
        def play6(): 
            pygame.mixer.music.load("D://rudiments//Double_Stroke_Roll.mp3")
            pygame.mixer.music.play(loops=0)
        def play7(): 
            pygame.mixer.music.load("D://rudiments//5_Stroke_Roll__open.mp3")
            pygame.mixer.music.play(loops=0)
        def play8(): 
            pygame.mixer.music.load("D://rudiments//6_Stroke_Roll__open.mp3")
            pygame.mixer.music.play(loops=0)
        def play9(): 
            pygame.mixer.music.load("D://rudiments//7_Stroke_Roll__open.mp3")
            pygame.mixer.music.play(loops=0)
        def play10(): 
            pygame.mixer.music.load("D://rudiments//9_Stroke_Roll__open.mp3")
            pygame.mixer.music.play(loops=0)
        def play11(): 
            pygame.mixer.music.load("D://rudiments//10_Stroke_Roll__open.mp3")
            pygame.mixer.music.play(loops=0)
        def play12(): 
            pygame.mixer.music.load("D://rudiments//11_Stroke_Roll__open.mp3")
            pygame.mixer.music.play(loops=0)    
        def play13(): 
            pygame.mixer.music.load("D://rudiments//13_Stroke_Roll__open.mp3")
            pygame.mixer.music.play(loops=0)
        def play14(): 
            pygame.mixer.music.load("D://rudiments//15_Stroke_Roll__open.mp3")
            pygame.mixer.music.play(loops=0)
        def play15(): 
            pygame.mixer.music.load("D://rudiments//17_Stroke_Roll__open.mp3")
            pygame.mixer.music.play(loops=0)    
        def play16(): 
            pygame.mixer.music.load("D://rudiments//Single_Paradiddle.mp3")
            pygame.mixer.music.play(loops=0)
        def play17(): 
            pygame.mixer.music.load("D://rudiments//Double_Paradiddle.mp3")
            pygame.mixer.music.play(loops=0)
        def play18(): 
            pygame.mixer.music.load("D://rudiments//Triple_Paradiddle.mp3")
            pygame.mixer.music.play(loops=0)
        def play19(): 
            pygame.mixer.music.load("D://rudiments//Single_Paradiddle-diddle.mp3")
            pygame.mixer.music.play(loops=0)
        def play20(): 
            pygame.mixer.music.load("D://rudiments//Flam.mp3")
            pygame.mixer.music.play(loops=0)
        def play21(): 
            pygame.mixer.music.load("D://rudiments//Flam_Accent.mp3")
            pygame.mixer.music.play(loops=0)
        def play22(): 
            pygame.mixer.music.load("D://rudiments//Flam_Tap.mp3")
            pygame.mixer.music.play(loops=0)
        def play23(): 
            pygame.mixer.music.load("D://rudiments//Flamacue.mp3")
            pygame.mixer.music.play(loops=0)
        def play24(): 
            pygame.mixer.music.load("D://rudiments//Flam_Paradiddle.mp3")
            pygame.mixer.music.play(loops=0)
        def play25(): 
            pygame.mixer.music.load("D://rudiments//Single_Flammed_Mill.mp3")
            pygame.mixer.music.play(loops=0)
        def play26(): 
            pygame.mixer.music.load("D://rudiments//Flam_Paradiddle-diddle.mp3")
            pygame.mixer.music.play(loops=0)
        def play27(): 
            pygame.mixer.music.load("D://rudiments//Pataflafla.mp3")
            pygame.mixer.music.play(loops=0)
        def play28(): 
            pygame.mixer.music.load("D://rudiments//Swiss_Army_Triplet.mp3")
            pygame.mixer.music.play(loops=0)
        def play29(): 
            pygame.mixer.music.load("D://rudiments//Inverted_Flam_Tap.mp3")
            pygame.mixer.music.play(loops=0)
        def play30(): 
            pygame.mixer.music.load("D://rudiments//Flam_Drag.mp3")
            pygame.mixer.music.play(loops=0)
        def play31(): 
            pygame.mixer.music.load("D://rudiments//Drag__open.mp3")
            pygame.mixer.music.play(loops=0)
        def play32(): 
            pygame.mixer.music.load("D://rudiments//Single_Drag_Tap__open.mp3")
            pygame.mixer.music.play(loops=0)    
        def play33(): 
            pygame.mixer.music.load("D://rudiments//Double_Drag_Tap__open.mp3")
            pygame.mixer.music.play(loops=0)
        def play34(): 
            pygame.mixer.music.load("D://rudiments//Lesson_25__open.mp3")
            pygame.mixer.music.play(loops=0)
        def play35(): 
            pygame.mixer.music.load("D://rudiments//Single_Dragadiddle.mp3")
            pygame.mixer.music.play(loops=0)    
        def play36(): 
            pygame.mixer.music.load("D://rudiments//Drag_Paradiddle__open.mp3")
            pygame.mixer.music.play(loops=0)
        def play37(): 
            pygame.mixer.music.load("D://rudiments//Drag_Paradiddle_2__open.mp3")
            pygame.mixer.music.play(loops=0)
        def play38(): 
            pygame.mixer.music.load("D://rudiments//Single_Ratamacue__open.mp3")
            pygame.mixer.music.play(loops=0)
        def play39(): 
            pygame.mixer.music.load("D://rudiments//Double_Ratamacue__open.mp3")
            pygame.mixer.music.play(loops=0)
        def play40(): 
            pygame.mixer.music.load("D://rudiments//Triple_Ratamacue__open.mp3")
            pygame.mixer.music.play(loops=0)
        def stop():
            pygame.mixer.music.stop()
            
        def RudimentsPlayer1():
            newWindow = Toplevel(master)
            newWindow.title("SINGLE STROKE ROLL")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play1()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play1)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//111.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer2():
            newWindow = Toplevel(master)
            newWindow.title("SINGLE STROKE FOUR")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play2()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play2)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//2.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer3():
            newWindow = Toplevel(master)
            newWindow.title("SINGLE STROKE SEVEN")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play3()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play3)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//3.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer4():
            newWindow = Toplevel(master)
            newWindow.title("MULTIPLE BOUNCE ROLL")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play4()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play4)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//4.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer5():
            newWindow = Toplevel(master)
            newWindow.title("TRIPLE STROKE ROLL")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play5()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play5)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//5.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer6():
            newWindow = Toplevel(master)
            newWindow.title("DOUBLE STROKE ROLL")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play6()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play6)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//6.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer7():
            newWindow = Toplevel(master)
            newWindow.title("FIVE STROKE ROLL")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play7()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play7)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//7.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer8():
            newWindow = Toplevel(master)
            newWindow.title("SIX STROKE ROLL")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play8()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play8)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//8.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer9():
            newWindow = Toplevel(master)
            newWindow.title("SEVEN STROKE ROLL")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play9()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play9)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//9.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer10():
            newWindow = Toplevel(master)
            newWindow.title("NINE STROKE ROLL")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play10()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play10)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//10.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer11():
            newWindow = Toplevel(master)
            newWindow.title("TEN STROKE ROLL")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play11()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play11)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//11.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer12():
            newWindow = Toplevel(master)
            newWindow.title("ELEVEN STROKE ROLL")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play12()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play12)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//12.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer13():
            newWindow = Toplevel(master)
            newWindow.title("THIRTEEN STROKE ROLL")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play13()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play13)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//13.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer14():
            newWindow = Toplevel(master)
            newWindow.title("FIFTEEN STROKE ROLL")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play14()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play14)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//14.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer15():
            newWindow = Toplevel(master)
            newWindow.title("SEVENTEEN STROKE ROLL")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play15()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play15)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//15.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer16():
            newWindow = Toplevel(master)
            newWindow.title("SINGLE PARADIDDLE")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play16()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play16)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//16.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer17():
            newWindow = Toplevel(master)
            newWindow.title("DOUBLE PARADIDDLE")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play17()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play17)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//17.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer18():
            newWindow = Toplevel(master)
            newWindow.title("TRIPLE PARADIDDLE")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play18()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play18)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//18.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer19():
            newWindow = Toplevel(master)
            newWindow.title("PARADIDDLE-DIDDLE")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play19()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play19)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//19.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer20():
            newWindow = Toplevel(master)
            newWindow.title("FLAM")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play20()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play20)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//20.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer21():
            newWindow = Toplevel(master)
            newWindow.title("FLAM ACCENT")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play21()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play21)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//21.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer22():
            newWindow = Toplevel(master)
            newWindow.title("FLAM TAP")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play22()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play22)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//22.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer23():
            newWindow = Toplevel(master)
            newWindow.title("FLAMACUE")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play23()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play23)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//23.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer24():
            newWindow = Toplevel(master)
            newWindow.title("FLAM PARADIDDLE")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play24()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play24)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//24.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer25():
            newWindow = Toplevel(master)
            newWindow.title("FLAMMED MILL")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play25()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play25)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//25.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer26():
            newWindow = Toplevel(master)
            newWindow.title("FLAM PARADIDDLE-DIDDLE")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play26()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play26)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//26.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer27():
            newWindow = Toplevel(master)
            newWindow.title("PATAFLA-FLA")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play27()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play27)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//27.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer28():
            newWindow = Toplevel(master)
            newWindow.title("SWISS ARMY TRIPLET")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play28()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play28)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//28.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer29():
            newWindow = Toplevel(master)
            newWindow.title("INVERTED FLAM TAP")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play29()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play29)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//29.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer30():
            newWindow = Toplevel(master)
            newWindow.title("FLAM DRAG")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play30()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play30)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//30.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer31():
            newWindow = Toplevel(master)
            newWindow.title("DRAG")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play31()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play31)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//31.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer32():
            newWindow = Toplevel(master)
            newWindow.title("SINGLE DRAG TAP")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play32()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play32)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//32.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer33():
            newWindow = Toplevel(master)
            newWindow.title("DOUBLE DRAG TAP")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play33()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play33)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//33.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer34():
            newWindow = Toplevel(master)
            newWindow.title("LESSON 25")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play34()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play34)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//34.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer35():
            newWindow = Toplevel(master)
            newWindow.title("SINGLE DRAGADIDDLE")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play35()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play35)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//35.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer36():
            newWindow = Toplevel(master)
            newWindow.title("DRAG PADADIDDLE #1")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play36()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play36)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//36.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer37():
            newWindow = Toplevel(master)
            newWindow.title("DRAG PARADIDDLE #2")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play37()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play37)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//37.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer38():
            newWindow = Toplevel(master)
            newWindow.title("SINGLE RATAMACUE")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play38()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play38)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//38.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer39():
            newWindow = Toplevel(master)
            newWindow.title("DOUBLE RATAMACUE")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play39()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play39)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//39.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        def RudimentsPlayer40():
            newWindow = Toplevel(master)
            newWindow.title("TRIPLE RATAMACUE")
            newWindow.geometry("600x400")
            newWindow.configure(bg='white')
            play40()
            stop_button = tk.Button(newWindow,text ='stop',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =stop)
            stop_button.pack()
            stop_button.place(x=180,y=300,height=50, width=100)
            repeat_button = tk.Button(newWindow,text ='Repeat',bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command =play40)
            repeat_button.pack()
            repeat_button.place(x=320,y=300,height=50, width=100)
            img=PhotoImage(file='D://rudipics//40.png')
            lbl=Label(newWindow,image=img,)
            lbl.image = img
            lbl.pack(pady=80)
        
        
        btn1 = tk.Button(master, text="SINGLE STROKE ROLL",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer1)
        btn1.pack(pady = 2)
        btn1.place(x=80,y=60)
        btn2 = tk.Button(master, text="SINGLE STROKE FOUR",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer2)
        btn2.pack(pady=2)
        btn2.place(x=80,y=121)
        btn3 = tk.Button(master, text="SINGLE STROKE SEVEN",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer3)
        btn3.pack(pady =2)
        btn3.place(x=80,y=180)
        btn4 = tk.Button(master, text="MULTIPLE BOUNCE ROLL",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer4)
        btn4.pack(pady =2)
        btn4.place(x=80,y=240)
        btn5 = tk.Button(master, text="TRIPLE STROKE ROLL",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer5)
        btn5.pack(pady =2)
        btn5.place(x=80,y=300)
        btn6 = tk.Button(master, text="DOUBLE STROKE ROLL",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer6)
        btn6.pack(pady =2)
        btn6.place(x=80,y=360)
        btn7 = tk.Button(master, text="FIVE STROKE ROLL",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer7)
        btn7.pack(pady =2)
        btn7.place(x=80,y=421)
        btn8 = tk.Button(master, text="SIX STROKE ROLL",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer8)
        btn8.pack(pady =2)
        btn8.place(x=80,y=480)
        btn9 = tk.Button(master, text="SEVEN STROKE ROLL",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer9)
        btn9.pack(pady =2)
        btn9.place(x=80,y=540)
        btn10 = tk.Button(master, text="NINE STROKE ROLL",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer10)
        btn10.pack(pady =2)
        btn10.place(x=80,y=600)
        btn11 = tk.Button(master, text="TEN STROKE ROLL",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer11)
        btn11.pack(pady =2)
        btn11.place(x=240,y=60)
        btn12 = tk.Button(master, text="ELEVEN STROKE ROLL",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer12)
        btn12.pack(pady=2)
        btn12.place(x=240,y=121)
        btn13 = tk.Button(master, text="THIRTEEN STROKE ROLL",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer13)
        btn13.pack(pady =2)
        btn13.place(x=240,y=180)
        btn14 = tk.Button(master, text="FIFTEEN STROKE ROLL",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer14)
        btn14.pack(pady =2)
        btn14.place(x=240,y=240)
        btn15 = tk.Button(master, text="SEVENTEEN STROKE ROLL",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer15)
        btn15.pack(pady =2)
        btn15.place(x=240,y=300)
        btn16 = tk.Button(master, text="SINGLE PARADIDDLE",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer16)
        btn16.pack(pady =2)
        btn16.place(x=240,y=360)
        btn17 = tk.Button(master, text="DOUBLE PARADIDDLE",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer17)
        btn17.pack(pady =2)
        btn17.place(x=240,y=421)
        btn18 = tk.Button(master, text="TRIPLE PARADIDDLE",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer18)
        btn18.pack(pady =2)
        btn18.place(x=240,y=480)
        btn19 = tk.Button(master, text="PARADIDDLE-DIDDLE",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer19)
        btn19.pack(pady =2)
        btn19.place(x=240,y=540)
        btn21 = tk.Button(master, text="FLAM",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer20)
        btn21.pack(pady =2)
        btn21.place(x=240,y=600)
        btn21 = tk.Button(master, text="FLAM ACCENT",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer21)
        btn21.pack(pady =2)
        btn21.place(x=521,y=60)
        btn22 = tk.Button(master, text="FLAM TAP",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer22)
        btn22.pack(pady=2)
        btn22.place(x=521,y=121)
        btn23 = tk.Button(master, text="FLAMACUE",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer32)
        btn23.pack(pady =2)
        btn23.place(x=521,y=180)
        btn24 = tk.Button(master, text="FLAM PARADIDDLE",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer24)
        btn24.pack(pady =2)
        btn24.place(x=521,y=240)
        btn25 = tk.Button(master, text="FLAMMED MILL",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer25)
        btn25.pack(pady =2)
        btn25.place(x=521,y=300)
        btn26 = tk.Button(master, text="FLAM PARADIDDLE-DIDDLE",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer26)
        btn26.pack(pady =2)
        btn26.place(x=521,y=360)
        btn27 = tk.Button(master, text="PATAFLA-FLA",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer27)
        btn27.pack(pady =2)
        btn27.place(x=521,y=421)
        btn28 = tk.Button(master, text="SWISS ARMY TRIPLET",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer28)
        btn28.pack(pady =2)
        btn28.place(x=521,y=480)
        btn29 = tk.Button(master, text="INVERTED FLAM TAP",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer29)
        btn29.pack(pady =2)
        btn29.place(x=521,y=540)
        btn30 = tk.Button(master, text="FLAM DRAG",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer30)
        btn30.pack(pady =2)
        btn30.place(x=521,y=600)
        btn31 = tk.Button(master, text="DRAG",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer31)
        btn31.pack(pady =2)
        btn31.place(x=680,y=60)
        btn32 = tk.Button(master, text="SINGLE DRAG TAP",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer32)
        btn32.pack(pady=2)
        btn32.place(x=680,y=121)
        btn33 = tk.Button(master, text="DOUBLE DRAG TAP",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer33)
        btn33.pack(pady =2)
        btn33.place(x=680,y=180)
        btn34 = tk.Button(master, text="LESSON 25",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer34)
        btn34.pack(pady =2)
        btn34.place(x=680,y=240)
        btn35 = tk.Button(master, text="SINGLE DRAGADIDDLE",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer35)
        btn35.pack(pady =2)
        btn35.place(x=680,y=300)
        btn36 = tk.Button(master, text="DRAG PADADIDDLE #1",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer36)
        btn36.pack(pady =2)
        btn36.place(x=680,y=360)
        btn37 = tk.Button(master, text="DRAG PARADIDDLE #2",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer37)
        btn37.pack(pady =2)
        btn37.place(x=680,y=421)
        btn38 = tk.Button(master, text="SINGLE RATAMACUE",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer38)
        btn38.pack(pady =2)
        btn38.place(x=680,y=480)
        btn39 = tk.Button(master, text="DOUBLE RATAMACUE",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer39)
        btn39.pack(pady =2)
        btn39.place(x=680,y=540)
        btn40 = tk.Button(master, text="TRIPLE RATAMACUE",width=21,height=3, bg="#e91e63",fg="white",borderwidth=0,activebackground="plum4",command=RudimentsPlayer40)
        btn40.pack(pady =2)
        btn40.place(x=680,y=600)
        master.mainloop()
    
    def PlaywithMouse():
        root2 = Toplevel(root)
        root2.title('Playing Using keyboard/mouse')
        root2_width = 900 
        root2_height = 700 
        
        screen_width= root2.winfo_screenwidth()
        screen_height= root2.winfo_screenheight()
        x= (screen_width/2) - (root2_width/2)
        y= (screen_height/2) - (root2_height/2)
        root2.geometry(f'{root2_width}x{root2_height}+{int(x)}+{int(y)}')
        root2.resizable(False, False)
        root2.iconbitmap('D://back/icon.ico')
        
        
        
        canvas1 = Canvas( root2, width =900,
                         height = 700)
        canvas1.pack(fill = "both", expand = True)
        bg = PhotoImage( file = "D://back//background.png")
        canvas1.create_image( 0, 0, image = bg, 
                             anchor = "nw")
        
        img = ImageTk.PhotoImage(Image.open("D://drums_pics//bass.png"))
        img_1 = ImageTk.PhotoImage(Image.open("D://drums_pics//crash.png"))
        img_2 = ImageTk.PhotoImage(Image.open("D://drums_pics//floor.png"))
        img_3 = ImageTk.PhotoImage(Image.open("D://drums_pics//tom.png"))
        img_4 = ImageTk.PhotoImage(Image.open("D://drums_pics//tom2.png"))
        img_5 = ImageTk.PhotoImage(Image.open("D://drums_pics//snare.png"))
        img_6 = ImageTk.PhotoImage(Image.open("D://drums_pics//hihat.png"))
        img_7 = ImageTk.PhotoImage(Image.open("D://drums_pics//ride.png"))
        
        
        def ClickTom(event):
            winsound.PlaySound("D://SoundsSynthesis//TOM1.wav",winsound.SND_ASYNC)
        def ClickSnare(event):
            winsound.PlaySound("D://SoundsSynthesis//SNARE.wav",winsound.SND_ASYNC)
        def ClickTom2(event):
            winsound.PlaySound("D://SoundsSynthesis//TOM2.wav",winsound.SND_ASYNC)
        def ClickHihat(event):
            winsound.PlaySound("D://SoundsSynthesis//HIHAT.wav",winsound.SND_ASYNC)
        def ClickFloor(event):
            winsound.PlaySound("D://SoundsSynthesis//FLOOR.wav",winsound.SND_ASYNC)
        def ClickBass(event):
            winsound.PlaySound("D://SoundsSynthesis//BASS.wav",winsound.SND_ASYNC)
        def ClickCrash(event):
            winsound.PlaySound("D://SoundsSynthesis//CRASH.wav",winsound.SND_ASYNC)
        def ClickRide(event):
            winsound.PlaySound("D://SoundsSynthesis//RIDE.wav",winsound.SND_ASYNC) 
        
        
                
                
                
        
                
         
        
               
        def clickerHihat(event):  
            winsound.PlaySound("D://SoundsSynthesis//SNARE.wav",winsound.SND_ASYNC)     
        
        def clickerBase(event):
            if  event.keysym == '??':
                winsound.PlaySound("D://SoundsSynthesis//BASS.wav",winsound.SND_ASYNC) 
           
        def clickerTom(event):
            if  event.keysym == '??':
                winsound.PlaySound("D://SoundsSynthesis//TOM1.wav",winsound.SND_ASYNC) 
        
           
        def clickerSnare(event):
            if  event.keysym == '??':
                winsound.PlaySound("D://SoundsSynthesis//SNARE.wav",winsound.SND_ASYNC) 
        
         
        def clickerTom2(event):
            if  event.keysym == '??':
                winsound.PlaySound("D://SoundsSynthesis//TOM2.wav",winsound.SND_ASYNC) 
        
        def clickerRide(event):
            if  event.keysym == '??':
                winsound.PlaySound("D://SoundsSynthesis//RIDE.wav",winsound.SND_ASYNC) 
        
        def clickerFloor(event):
            if  event.keysym == '??':
                winsound.PlaySound("D://SoundsSynthesis//FLOOR.wav",winsound.SND_ASYNC) 
             
                
        def clickerCrash(event):
            if  event.keysym == '??':
                winsound.PlaySound("D://SoundsSynthesis//CRASH.wav",winsound.SND_ASYNC)
            
        
        '''
        myB = Button(root2 , text = "click me" )
        myB.bind("<Key>" , clicker)
        '''
        
        
        
        tom = tk.Button(root2 , image = img_3 ,activebackground="plum4")
        tom.bind("<Button-1>" , clickerTom)
        
        
        crash = tk.Button(root2 , image = img_1 ,activebackground="gold" )
        crash.bind("<Button-1>" , clickerCrash)
        
        
        tom2 = tk.Button(root2 , image = img_4 ,activebackground="navy")
        tom2.bind("<Button-1>" , clickerTom2)
        
        
        ride = tk.Button(root2 , image = img_7,activebackground="cyan" )
        ride.bind("<Button-1>" ,clickerRide )
        
        
        snare = tk.Button(root2 , image = img_5 ,activebackground="coral")
        snare.bind("<Button-1>" , clickerSnare)
        
        
        hihat = tk.Button(root2 , image = img_6 ,activebackground="gray")
        hihat.bind("<Button-1>" , clickerHihat)
        
        
        floor = tk.Button(root2 , image = img_2 ,activebackground="red" )
        floor.bind("<Button-1>" , clickerFloor)
        
        
        base = tk.Button(root2 , image = img ,activebackground="green")
        base.bind("<Button-1>" , clickerBase)
        
        
        root2.bind("<q>",ClickTom) 
        root2.bind("<w>",ClickSnare)
        root2.bind("<e>",ClickTom2)
        root2.bind("<r>",ClickHihat)
        root2.bind("<t>",ClickFloor)
        root2.bind("<y>",ClickBass)
        root2.bind("<u>",ClickCrash)
        root2.bind("<i>",ClickRide)
        
        
        
        
        button1_canvas = canvas1.create_window( 50 , 150, 
                                               anchor = "nw",
                                               window = tom)
        
        button2_canvas = canvas1.create_window( 250, 150 ,
                                               anchor = "nw",
                                                window = crash)
        
        button3_canvas = canvas1.create_window( 450 , 150 ,
                                               anchor = "nw",
                                               window = tom2)
        
        button4_canvas = canvas1.create_window( 50 , 350 ,
                                               anchor = "nw",
                                               window = ride)
        
        button5_canvas = canvas1.create_window( 250 , 350, 
                                               anchor = "nw",
                                               window = snare)
        
        button6_canvas = canvas1.create_window( 650, 150 ,
                                               anchor = "nw",
                                               window = hihat)
        
        button7_canvas = canvas1.create_window( 450 , 350 ,
                                               anchor = "nw",
                                               window = floor)
        
        button8_canvas = canvas1.create_window( 650 , 350 ,
                                               anchor = "nw",
                                               window = base)
        
        root2.mainloop()
    
    def Exit():
        root.destroy()
        
        
    btn_camera = tk.Button(root, text="Play Using Camera",width=30,height=5, bg="#e91e63",fg="white",borderwidth=1,activebackground="plum4",command=PlayWithCamera)
    btn_camera.pack(pady = 2)
    btn_camera.place(x=350,y=230)
    btn_rudiments = tk.Button(root, text="40 Rudiments",width=30,height=5, bg="#e91e63",fg="white",borderwidth=1,activebackground="plum4",command=Rudiments)
    btn_rudiments.pack(pady = 2)
    btn_rudiments.place(x=350,y=340)
    btn_mouse = tk.Button(root, text="Play Using Keyboard/mouse",width=30,height=5, bg="#e91e63",fg="white",borderwidth=1,activebackground="plum4",command=PlaywithMouse)
    btn_mouse.pack(pady = 2)
    btn_mouse.place(x=350,y=450)
    btn_exit = tk.Button(root, text="Exit",width=30,height=5, bg="#e91e63",fg="white",borderwidth=1,activebackground="plum4",command=Exit)
    btn_exit.pack(pady = 2)
    btn_exit.place(x=350,y=560)
            
    
    
    root.mainloop()

    
splash_root.after(4000,mainPage)
    
mainloop()