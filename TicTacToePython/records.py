import TicTacToePython.dbhelpermongo as dbhelper
try:
    # for Python2
    import Tkinter as tk
except ImportError:
    # for Python3
    import tkinter as tk

class Records(tk.Frame):
    """Records GUI and Database"""
    """TODO
        Separate into DB access (model), GUI (view) and controller
    """
    def __init__(self,master,onclick_back=None):
        tk.Frame.__init__(self, master)
        self.panel = tk.Frame(self)
        self.panel.pack()
        self.quit_btn = tk.Button(self.panel,text="Back",command=lambda:onclick_back(self))
        self.quit_btn.pack(side="left")
        self.clear_btn = tk.Button(self.panel,text="Clear",command=self.onclick_clear)
        self.clear_btn.pack(side="left")
        self.populate()

    def populate(self):
        self.list = tk.Frame(self)
        self.list.pack(fill="both")
        
        timestamp_header = tk.Label(self.list,text="Timestamp")
        timestamp_header.grid(row=0,column=0)
        duration_header = tk.Label(self.list,text="Duration")
        duration_header.grid(row=0,column=1)
        winner_header = tk.Label(self.list,text="Winner")
        winner_header.grid(row=0,column=2)

        index = 1
        for record in dbhelper.get_all_records():
            timestamp = tk.Label(self.list,text="{:%d %b %Y %H:%M:%S}".format(record["timestamp"]))
            timestamp.grid(row=index,column=0)
            duration = tk.Label(self.list,text=record["duration"])
            duration.grid(row=index,column=1)
            winner = tk.Label(self.list,text=record["winner"])
            winner.grid(row=index,column=2)
            index = index + 1

    def onclick_clear(self):
        dbhelper.remove_all_records()
        self.list.pack_forget()
        self.populate()