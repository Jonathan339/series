from tkinter import Tk, Label, Button, Listbox

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("vercion 0.0.20")

        self.label = Label(master, text="")
        self.label.pack()

        self.lbprogramacion = Label(master, text="Programación")
        self.lbprogramacion.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()