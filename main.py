from view import View
from tkinter import*
from tkinter.tix import*
import model
import controller as controller
import view

if __name__ == "__main__":

    window = Tk()
    model = model.Model()
    controller = controller.Controller(model)
    app = View(window,controller)
    
    window.mainloop()