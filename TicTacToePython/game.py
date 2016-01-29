try:
    # for Python2
    import Tkinter as tk
except ImportError:
    # for Python3
    import tkinter as tk

class Game(tk.Frame):
    """TicTacToe Game logic and GUI"""
    def __init__(self,master,onclick_back=None):
        tk.Frame.__init__(self, master)
        self.blank_img = tk.PhotoImage(file="img/blank.gif")
        self.x_img = tk.PhotoImage(file="img/x.gif")
        self.o_img = tk.PhotoImage(file="img/o.gif")
        self.xwin_img = tk.PhotoImage(file="img/xwin.gif")
        self.owin_img = tk.PhotoImage(file="img/owin.gif")
        self.panel = tk.Frame(self)
        self.panel.grid(row=0)
        self.quit_btn = tk.Button(self.panel,text="Back",command=onclick_back)
        self.quit_btn.pack(side="left")
        self.reset_btn = tk.Button(self.panel,text="Reset",command=self.reset)
        self.reset_btn.pack(side="left")
        self.turn_lbl = tk.Label(self.panel,text="Turn ",image=self.x_img,compound="right")
        self.turn_lbl.pack(side="left")
        self.duration = 0
        self.duration_label = tk.Label(self.panel)
        self.duration_label.pack(side="left")
        self.canvas = tk.Canvas(self,height=150,width=150)
        self.canvas.grid(row=1)
        self.reset()

    # Reset game variables to initial state
    def reset(self):
        self.duration = 0
        self.duration_label.configure(text="Duration: %s"%str(self.duration))
        self.turn = 'x'
        self.turn_lbl.configure(image=self.x_img)
        self.game_started = False
        self.game_ended = False
        self.board= []
        for i in range(0,9):
            space = BoardSpace(self.canvas,i,self.blank_img,self.onclick_board)
            self.board.append(space)

    def onclick_board(self,clicked):
        # Do nothing if space already taken
        if clicked.value != "blank":
            return
        if self.game_ended:
            return

        # If game isn't started, start it and timer
        if self.game_started == False:
            self.game_started = True
            self.after(1000,self.ontick_duration)

        if(self.turn == 'x'):
            clicked.btn.configure(image=self.x_img)
            clicked.value = "x"
            self.turn = 'o'
            self.turn_lbl.configure(image=self.o_img)
        else:
            clicked.btn.configure(image=self.o_img)
            clicked.value = "o"
            self.turn = 'x'
            self.turn_lbl.configure(image=self.x_img)
        
        self.winner = self.check_winner_row(self.board[0], self.board[1], self.board[2]) or \
        self.check_winner_row(self.board[3], self.board[4], self.board[5]) or\
        self.check_winner_row(self.board[6], self.board[7], self.board[8]) or\
        self.check_winner_row(self.board[0], self.board[3], self.board[6]) or\
        self.check_winner_row(self.board[1], self.board[4], self.board[7]) or\
        self.check_winner_row(self.board[2], self.board[5], self.board[8]) or\
        self.check_winner_row(self.board[0], self.board[4], self.board[8]) or\
        self.check_winner_row(self.board[2], self.board[4], self.board[6]);

    # Every second, update the duration
    def ontick_duration(self):
        if(self.game_ended):
            return

        self.duration = self.duration + 1
        self.duration_label.configure(text="Duration: %s"%str(self.duration))
        self.after(1000,self.ontick_duration)

    def check_winner_row(self,p1,p2,p3):
        if(p1.value == p2.value and p2.value == p3.value):
            if(p1.value == "x"):
                self.game_ended = True
                p1.btn.configure(image=self.xwin_img)
                p2.btn.configure(image=self.xwin_img)
                p3.btn.configure(image=self.xwin_img)
            elif(p1.value == "o"):
                self.game_ended = True
                p1.btn.configure(image=self.owin_img)
                p2.btn.configure(image=self.owin_img)
                p3.btn.configure(image=self.owin_img)

class BoardSpace(object):
    def __init__(self,master,index,img,onclick):
        self.index = index
        self.btn = tk.Button(master,image=img,command=lambda:onclick(self))
        self.btn.grid(row=int(index/3),column=int(index%3))
        self.value = "blank"