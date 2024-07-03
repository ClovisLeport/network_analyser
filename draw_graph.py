import tkinter as tk
from tkinter import Label, BOTH
from network_analyser import get_devices
from PIL import Image, ImageTk
from ToolTip import HoverInfo
from device import Device
import math

def draw_graph():
    devices = [Device("192.168.88.1","52:55","Router"),Device("192.168.88.245","52:55","Dolclov"),Device("192.168.88.67","52:55","Clement"),
               Device("192.168.88.245","52:68","Titouan"),Device("192.168.88.69","52:68","Gabriel")]
    router = [ i for i in devices if i.name == "Router"]
    for i in router : devices.remove(i)
    window = tk.Tk()
    win_width = 800
    win_height = 600
    window.geometry(str(win_width)+"x"+str(win_height))
    window.title("Network Graph")

    image = ImageTk.PhotoImage(Image.open(r"C:\Users\clovi\OneDrive\Documents\network_analyser\network_analyser\images\router.png"))
    canvas = tk.Canvas(window, width=win_width, height=win_height)
    canvas.pack()
    canvas.create_image(win_width/2,win_height/2, image=image)
    label_text = "Router"
    canvas.create_text(win_width / 2, (win_height / 2) + (image.height() / 2)+20, text=label_text, font=("Helvetica", 16), fill="black")

    circle_diameter = 6000
    radius = circle_diameter / (2*math.pi)

    polar_dist = radius
    polar_angle = 360 / len(devices)

    for i in range(len(devices)):
        print(len(devices))
        image1 = Image.open(r"C:\Users\clovi\OneDrive\Documents\network_analyser\network_analyser\images\computer.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(image=test)
        label1.image = test
        x, y = radius * math.cos(polar_angle*i), radius * math.sin(polar_angle*i)
        label1.place(x=x, y=y)
        canvas.create_line(x, y, win_width/2, win_height/2, fill="grey", width=2)

    # Lancement de la boucle principale de l'interface
    window.mainloop()

draw_graph()