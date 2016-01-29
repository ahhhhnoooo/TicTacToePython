try:
    # for Python2
    import Tkinter as tk
except ImportError:
    # for Python3
    import tkinter as tk

class MainMenu(tk.Frame):
    """Main Menu GUI functions"""
    # Allow optional button callbacks
    def __init__(self,master,onclick_newgame=None,onclick_records=None,onclick_quit=None):
        tk.Frame.__init__(self, master)

        self.new_game_btn = tk.Button(self,text="New Game",command=onclick_newgame)
        self.new_game_btn.pack()
        self.records_btn = tk.Button(self,text="Records",command=onclick_records)
        self.records_btn.pack()
        self.quit_btn = tk.Button(self,text="Quit",command=onclick_quit)
        self.quit_btn.pack()