import TicTacToePython.game
import TicTacToePython.records
import TicTacToePython.mainmenu
try:
    # for Python2
    import Tkinter as tk
except ImportError:
    # for Python3
    import tkinter as tk

class App(object):
    def __init__(self):
        self.root = tk.Tk()

        self.menu = TicTacToePython.mainmenu.MainMenu(self.root,\
            onclick_newgame=self.onclick_newgame,\
            onclick_records=self.onclick_records,\
            onclick_quit=self.quit)
        self.menu.pack()
        self.root.mainloop()
        
    # New Game button clicked, hide mainmenu and show game
    def onclick_newgame(self):
        self.menu.pack_forget()
        self.game = TicTacToePython.game.Game(self.root,\
            onclick_back=self.back_to_mainmenu)
        self.game.pack()

    # Records button clicked, hide mainmenu and show records
    def onclick_records(self):
        self.menu.pack_forget()
        self.records = TicTacToePython.records.Records(self.root, \
            onclick_back=self.back_to_mainmenu)
        self.records.pack()
    
    # quit window and clean up
    def quit(self):
        self.root.quit()
        self.root.destroy()
    
    # Go back to mainmenu from game or records
    def back_to_mainmenu(self,sender):
        sender.pack_forget()
        self.menu.pack()