import tkinter as tk
from tkinter import Label, BOTH
from network_analyser import get_devices
from PIL import Image, ImageTk
from ToolTip import HoverInfo
from device import Device
import math
import numpy as np

PATH_IMAGES = r"C:\Users\clovi\OneDrive\Documents\network_analyser\network_analyser\images"
class Application:
    def __init__(self, window):
        self.zoom_factor = 1.0
        devices = [Device("192.168.88.1","52:55","Router"),Device("192.168.88.245","52:55","Dolclov"),Device("192.168.88.67","52:55","Clement"),
                Device("192.168.88.70","52:68","Titouan"),Device("192.168.88.69","52:68","Gabriel"),Device("192.168.88.69","52:68","192.168.88.69")]
        
        router = [ i for i in devices if i.name == "Router"]
        for i in router : devices.remove(i)
        self.window = window
        win_width = 800
        win_height = 600
        self.window.geometry(str(win_width)+"x"+str(win_height))
        self.window.title("Network Graph")


        image = ImageTk.PhotoImage(Image.open(PATH_IMAGES+r"\router.png"))
        self.canvas_x = 0
        self.canvas_y = 0
        self.canvas = tk.Canvas(self.window, width=win_width, height=win_height)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.create_image(win_width/2,win_height/2, image=image)
        label_text = "Router"
        self.canvas.create_text(win_width / 2, (win_height / 2) + (image.height() / 2)+20, text=label_text, font=("Helvetica", 16), fill="black")

        circle_diameter =image.height()*len(devices) *5
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
            image1 = Image.open(PATH_IMAGES+r"\computer.png")
            test = ImageTk.PhotoImage(image1)
            self.canvas.create_image(positions[i][0], positions[i][1], image=test)
            
            self.canvas.create_line(positions[i][0] + (positions[i][2]*0.3), positions[i][1]+ (positions[i][3]*0.3),
                                win_width/2- (positions[i][2]*0.15), win_height/2-(positions[i][3]*0.15), fill="grey", width=2)
            label_text = devices[i].name
            self.canvas.create_text(positions[i][0], positions[i][1]+ (image.height()/1.5), text=label_text, font=("Helvetica", 16), fill="black")
            image_list.append(test)
        self.window.mainloop()

    def zoom(self, event):        
        if event.delta > 0:
            self.canvas.scale("all", 0, 0, 1.1,1.1)
        elif event.delta < 0:
            self.canvas.scale("all", 0, 0, 0.9, 0.9)
        #self.canvas.scale("all", 0, 0, self.zoom_factor, self.zoom_factor)

    def on_key_press(self, event):
        # Déplacement du canvas avec les touches directionnelles
        if event.keysym == "Left":
            self.canvas.move("all", -10,0)
        elif event.keysym == "Right":
            self.canvas.move("all", 10,0)
        elif event.keysym == "Up":
            self.canvas.move("all", 0,-10)
        elif event.keysym == "Down":
            self.canvas.move("all", 0,10)
        
if __name__ == "__main__":
    window = tk.Tk()
    app = Application(window)
    window.mainloop()