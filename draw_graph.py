import tkinter as tk
from tkinter import Label, BOTH
from network_analyser import get_devices
from PIL import Image, ImageTk
from ToolTip import HoverInfo
from device import Device
def draw_graph():
    devices = [Device("192.168.88.1","52:55","Router"),Device("192.168.88.245","52:55","Dolclov"),Device("192.168.88.67","52:55","Clement")]
    router = [ i for i in devices if i.name == "Router"]
    for i in router : devices.remove(i)
    window = tk.Tk()
    win_width = 800
    win_height = 600
    window.geometry(str(win_width)+"x"+str(win_height))
    window.title("Network Graph")

    image = ImageTk.PhotoImage(Image.open(r"C:\Users\clovi\OneDrive\Documents\network_analyser\images\router.png"))
    canvas = tk.Canvas(window, width=win_width, height=win_height)
    canvas.pack()
    canvas.create_image(win_width/2,win_height/2, image=image)
    label_text = "Router"
    canvas.create_text(win_width / 2, (win_height / 2) + (image.height() / 2)+20, text=label_text, font=("Helvetica", 16), fill="black")

    for i in devices:
        image1 = Image.open(r"C:\Users\clovi\OneDrive\Documents\network_analyser\images\computer.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(image=test)
        label1.image = test
        # Position image
        label1.place(x=200, y=200)
        
        canvas1 = tk.Canvas(window, width=win_width, height=win_height)
        canvas1.create_line(200, 200, win_width/2,win_height/2, fill="green", width=5)
        canvas1.pack()

    # Lancement de la boucle principale de l'interface
    window.mainloop()

draw_graph()