from tkinter import*
from tkinter.tix import*

from tkinter import Label, BOTH
from model import Model
from device import Device
import math
from PIL import Image, ImageTk
from tktooltip import ToolTip
import numpy as np
from idlelib.tooltip import Hovertip

#from ToolTip import ToolTip, CreateToolTip
PATH_IMAGES = r"C:\Users\clovi\OneDrive\Documents\network_analyser\network_analyser\images"

class View:
    
    def __init__(self, window, controller):

        self.controller = controller

        devices = [Device("192.168.88.1","00:1B:44:11:3A:B7", "Router"),Device("192.168.88.245","00:1B:44:11:3A:B7", "Dolclov"),
                   Device("192.168.88.67","00:1B:44:11:3A:B7", "Clément"),Device("192.168.88.68","00:1B:44:11:3A:B7", "Titou"),
                   Device("192.168.88.245","00:1B:44:11:3A:B7", "Dolclov"),Device("192.168.88.67","00:1B:44:11:3A:B7", "Clément"),
                   Device("192.168.88.68","00:1B:44:11:3A:B7", "Titou"),
                   Device("192.168.88.245","00:1B:44:11:3A:B7", "Dolclov"),Device("192.168.88.67","00:1B:44:11:3A:B7", "Clément"),
                   Device("192.168.88.68","00:1B:44:11:3A:B7", "Titou"),
                   Device("192.168.88.245","00:1B:44:11:3A:B7", "Dolclov"),Device("192.168.88.67","00:1B:44:11:3A:B7", "Clément"),
                   Device("192.168.88.68","00:1B:44:11:3A:B7", "Titou"),
                   Device("192.168.88.245","00:1B:44:11:3A:B7", "Dolclov"),Device("192.168.88.67","00:1B:44:11:3A:B7", "Clément"),
                   Device("192.168.88.68","00:1B:44:11:3A:B7", "Titou"),]
        
        router = [ i for i in devices if i.name == "Router"]
        for i in router : devices.remove(i)
        self.window = window
        win_width = 800
        win_height = 600
        self.zoom_factor = 1.0
        self.window.geometry(str(win_width)+"x"+str(win_height))
        self.window.title("Network Graph")


        
        self.canvas_x = 0
        self.canvas_y = 0
        self.canvas = Canvas(self.window, width=win_width, height=win_height)
        self.canvas.pack(fill=BOTH, expand=True)
        image_router = PhotoImage(file = PATH_IMAGES+r'\router.png')

        for i in router:
            label = Label(self.canvas, image = image_router)
            label.pack()
            self.canvas.create_window(win_width/2,win_height/2, window=label)
            tip = Balloon(window,bg='grey87',initwait=50)
            informations = "Name : " + i.name + "\n" + "IP : " + i.ip+ "\n" +  "MAC Address : " + i.mac_address
            tip.bind_widget(label,balloonmsg=informations)
            self.canvas.create_text(win_width / 2, (win_height / 2) + (image_router.height() / 2)+(7*len(devices)), 
                                    text="Router", font=("Helvetica", 16), fill="black")

        circle_diameter =image_router.height()*len(devices) *5
        radius = circle_diameter / (2*math.pi)

        angles = np.linspace(0, 2 * np.pi, len(devices), endpoint=False)
        positions=[]
        for angle in angles:
            x = win_width/2 + radius * np.cos(angle)
            y = win_height/2 + radius * np.sin(angle)
            positions.append((x, y, win_width/2-x,win_height/2-y  ))

        self.canvas.bind("<MouseWheel>", self.zoom)
        self.window.bind("<KeyPress>", self.on_key_press)

        image_list= []
        for i in range(len(positions)):
                        
            image_tip= PhotoImage(file = PATH_IMAGES+'\computer.png')
            label = Label(self.canvas, image = image_tip)
            label.pack()
            self.canvas.create_window(positions[i][0], positions[i][1], window=label)
            self.canvas.create_line(positions[i][0] + (positions[i][2]*0.15), positions[i][1]+ (positions[i][3]*0.15),
                                win_width/2- (positions[i][2]*0.3), win_height/2-(positions[i][3]*0.3), fill="grey", width=2)
            label_text = devices[i].name if "NaN" not in devices[i].name else devices[i].ip
            self.canvas.create_text(positions[i][0]-(positions[i][2]*0.35) , positions[i][1]-(positions[i][3]*0.35), 
                                    text=label_text, font=("Helvetica", 16), fill="black")
            image_list.append(image_tip)

            tip = Balloon(self.window,bg='grey87',initwait=50)
            informations = "Name : " + devices[i].name + "\n" + "IP : " + devices[i].ip+ "\n" +  "MAC Address : " + devices[i].mac_address
            tip.bind_widget(label,balloonmsg=informations)
        self.window.mainloop()

    def zoom(self, event):        
        if event.delta > 0:
            self.canvas.scale("all", 0, 0, 1.1,1.1)
            self.canvas.move("all", -30,-23)
        elif event.delta < 0:
            self.canvas.scale("all", 0, 0, 0.9, 0.9)
            self.canvas.move("all", 30,22)
        
    def on_key_press(self, event):
        if event.keysym == "Left":
            self.canvas.move("all", 10,0)
        elif event.keysym == "Right":
            self.canvas.move("all", -10,0)
        elif event.keysym == "Up":
            self.canvas.move("all", 0,10)
        elif event.keysym == "Down":
            self.canvas.move("all", 0,-10)
    
        
