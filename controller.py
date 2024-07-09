from device import Device

class Controller:

    def __init__(self,model):
        self.model = model
        self.view = None

    def zoom(self, event):        
        if event.delta > 0:
            self.view.canvas.scale("all", 0, 0, 1.1,1.1)
            self.view.canvas.move("all", -30,-23)
        elif event.delta < 0:
            self.view.canvas.scale("all", 0, 0, 0.9, 0.9)
            self.view.canvas.move("all", 30,22)

    def on_key_press(self, event):
        if event.keysym == "Left":
            self.view.canvas.move("all", 10,0)
        elif event.keysym == "Right":
            self.view.canvas.move("all", -10,0)
        elif event.keysym == "Up":
            self.view.canvas.move("all", 0,10)
        elif event.keysym == "Down":
            self.view.canvas.move("all", 0,-10)
        elif event.keysym=='r':
            self.view.canvas.delete('all')
            #self.view.devices = self.model.get_new_devices(self.view.devices)
            self.view.devices.append(Device("192.168.88.67","00:1B:44:11:3A:B7", "Clément"))
            self.view.create_router(self.view.router, self.view.window, self.view.image_router)
            self.image_list = self.view.create_devices(self.view.devices, self.view.positions,self.view.win_width,self.view.win_height, self.view.image_router )
