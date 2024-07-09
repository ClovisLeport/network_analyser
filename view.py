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
import Pmw

#from ToolTip import ToolTip, CreateToolTip
PATH_IMAGES = r"C:\Users\clovi\OneDrive\Documents\network_analyser\network_analyser\images"

class View:
    
    def __init__(self, window, controller):
        self.controller=controller
        self.controller.view = self
        self.devices = [Device("192.168.88.1","00:1B:44:11:3A:B7", "Router"),Device("192.168.88.245","00:1B:44:11:3A:B7", "Dolclov"),
                   Device("192.168.88.67","00:1B:44:11:3A:B7", "Clément")]
        
        self.router = [ i for i in self.devices if i.name == "Router"]
        for i in self.router : self.devices.remove(i)
        self.window = window
        self.win_width = 800
        self.win_height = 600
        self.zoom_factor = 1.0
        self.window.geometry(str(self.win_width)+"x"+str(self.win_height))
        self.window.title("Network Graph")
        self.positions=[]
        self.canvas_x = 0
        self.canvas_y = 0
        self.canvas = Canvas(self.window, width=self.win_width, height=self.win_height)
        self.canvas.pack(fill=BOTH, expand=True)
        self.image_router = PhotoImage(file = PATH_IMAGES+r'\router.png')
        self.create_router( self.router, self.window,self.image_router)
        

        self.canvas.bind("<MouseWheel>", self.controller.zoom)
        self.window.bind("<KeyPress>", self.controller.on_key_press)
        self.image_list = self.create_devices(self.devices, self.positions,self.win_width,self.win_height,self.image_router  )
    
        self.window.mainloop()


    def create_devices(self, devices, positions,win_width,win_height,image_router) -> list:

        image_list= []
        positions=[]
        circle_diameter =image_router.height()*len(devices) *5
        radius = circle_diameter / (2*math.pi)
        angles = np.linspace(0, 2 * np.pi, len(devices), endpoint=False)
        for angle in angles:
            x = win_width/2 + radius * np.cos(angle)
            y = win_height/2 + radius * np.sin(angle)
            positions.append((x, y, win_width/2-x, win_height/2-y  ))
        
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
            tip = Balloon(self.window,bg='black',initwait=50)

            informations = "Name : " + devices[i].name + "\n" + "IP : " + devices[i].ip+ "\n" +  "MAC Address : " + devices[i].mac_address
            tip.bind_widget(label,balloonmsg=informations)

        return image_list

    def create_router(self, router, window, image_router):
        
        for i in range(len(router)):
            tip = Balloon(window,bg='grey87',initwait=50)
            informations = "Name : " + router[i].name + "\n" + "IP : " + router[i].ip+ "\n" +  "MAC Address : " + router[i].mac_address
            # self.canvas.create_text(win_width / 2, (win_height / 2) + (image_router.height() / 2), 
            #                         text="Router", font=("Helvetica", 16), fill="black")
            label = Label(self.canvas, image = image_router)
            label.pack()
            self.canvas.create_window((self.win_width)/(2-i),self.win_height/2 , window=label)
            tip.bind_widget(label,balloonmsg=informations)
