try:
    # for Python2
    import Tkinter as tk
except ImportError:
    # for Python3
    import tkinter as tk

class Records(tk.Frame):
    """Records GUI"""
    
    def __init__(self,master,onclick_back=None):
        tk.Frame.__init__(self, master)
        self.quit_btn = tk.Button(self,text="Back",command=onclick_back)
        self.quit_btn.pack()
