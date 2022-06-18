
from cgitb import text
from doctest import master
import tkinter
from turtle import width
from PIL import Image,ImageTk

import TkinterCustomButton


import os.path
from os import path

import functions

class GUI(tkinter.Tk):

    funcs = None

    def removeplaceholder(event):
        event.widget.configure(state="normal")
        event.widget.delete(0, "end")
        event.widget.unbind('<Button-1>', event.widget.placeholder_rule_id)

    def selectall(event):
        # select text
        event.widget.select_range(0, 'end')
        # move cursor to the end
        event.widget.icursor('end')
        #stop propagation
        return 'break'

    def set_qrcode_image(self):
        self.layout.img = ImageTk.PhotoImage(master=self.layout, image=Image.open("qrcode.png").resize((200, 200)))
        self.layout.itemconfig(self.layout.img_id,image=self.layout.img)

    def generate(self):
        print( self.link.get()) 
        self.funcs.generate( self.link.get() )

    def set_issue_text(self, text):
        self.issue.set(text)

    def __init__(self):
        self.funcs = functions.funcs( self )
        super().__init__()
        self.title("KekwQRCode Generator")
        
        # Layout
        self.layout = tkinter.Canvas(master=self, width=640, height=360)
         
        self.layout.create_rectangle(0, 0, 150, 640, fill="#363945", outline="#363945")
        self.layout.create_rectangle(150, 0, 640, 360, fill="#F0EDE5", outline="#F0EDE5")


        # Border
        self.layout.create_rectangle(620-205, 340-205, 623, 343, fill="#F0EDE5", outline = '#363945', width=3)

        if (path.exists("qrcode.png")):
            self.layout.img = ImageTk.PhotoImage(master=self.layout, image=Image.open("qrcode.png").resize((200, 200)))
            self.layout.img_id = self.layout.create_image(320+200, 180+60, image=self.layout.img, anchor="center")
        else:
            self.layout.img_id = self.layout.create_image(320+200, 180+60, anchor="center")

        # Type

        self.types = tkinter.Label(self, justify="center", bd=0, fg="white", bg="#363945", text="Formats:", font=("Terminal", 10))
        self.layout.create_window(75, 18, window=self.types)

        self.svg_type = tkinter.IntVar()
        self.svg = tkinter.Checkbutton(self.layout, text='.svg', bg="#363945", fg="white", selectcolor="#939597", activebackground="#363945", activeforeground="white", highlightthickness=0,bd=0, variable=self.svg_type)
        self.svg_type.set( 0 )
        self.layout.create_window(40, 40, window=self.svg)

        self.png_type = tkinter.IntVar()
        self.png = tkinter.Checkbutton(self.layout, text='.png', bg="#363945", fg="white", selectcolor="#939597", activebackground="#363945", activeforeground="white", highlightthickness=0,bd=0, variable=self.png_type)
        self.png_type.set( 0 )
        self.layout.create_window(40, 60, window=self.png)

        self.jpg_type = tkinter.IntVar()
        self.jpg = tkinter.Checkbutton(self.layout, text='.jpg', bg="#363945", fg="white", selectcolor="#939597", activebackground="#363945", activeforeground="white", highlightthickness=0,bd=0, variable=self.jpg_type)
        self.jpg_type.set( 0 )
        self.layout.create_window(38, 80, window=self.jpg)

        self.html_type = tkinter.IntVar()
        self.html = tkinter.Checkbutton(self.layout, text='.html', bg="#363945", fg="white", selectcolor="#939597", activebackground="#363945", activeforeground="white", highlightthickness=0,bd=0, variable=self.html_type)
        self.html_type.set( 0 )
        self.layout.create_window(43, 100, window=self.html)

        # URL Entry

        link_label = tkinter.Label(self, justify="center", bd=0, bg="#F0EDE5", fg="#363945", text="URL:", font=("Roman", 10))
        self.layout.create_window(240, 45-24, window=link_label)  

        self.link = tkinter.Entry(self)
        self.layout.create_window(150+245, 45,window=self.link, width=345, height=24)
        self.link.insert(0, "https://www.doktorsas.xyz")
        self.link.bind('<Control-a>', GUI.selectall )
        self.link.placeholder_rule_id = self.link.bind('<Button-1>', GUI.removeplaceholder )
        self.link.root = self

        self.issue = tkinter.StringVar()
        self.issue_label = tkinter.Label(self, justify="center", bd=0, bg="#F0EDE5", fg="red", textvariable=self.issue, font=("Roman", 10))
        self.layout.create_window(150+245, 75, window=self.issue_label)  

        # Background color entry

        bgcolor_label = tkinter.Label(self, justify="center", bd=0, bg="#F0EDE5", fg="#363945", text="Background:", font=("Roman", 10))
        self.layout.create_window(220, 165-24, window=bgcolor_label)  

        self.bgcolor = tkinter.Entry(self)
        self.layout.create_window(220, 165,window=self.bgcolor, width=80, height=24)
        self.bgcolor.insert(0, "white")
        self.bgcolor.bind('<Control-a>', GUI.selectall )
        self.bgcolor.placeholder_rule_id = self.bgcolor.bind('<Button-1>', GUI.removeplaceholder )
        self.bgcolor.root = self


        fgcolor_label = tkinter.Label(self, justify="center", bd=0, bg="#F0EDE5", fg="#363945", text="Color:", font=("Roman", 10))
        self.layout.create_window(320, 165-24, window=fgcolor_label)  

        self.fgcolor = tkinter.Entry(self)
        self.layout.create_window(340, 165,window=self.fgcolor, width=80, height=24)
        self.fgcolor.insert(0, "black")
        self.fgcolor.bind('<Control-a>', GUI.selectall )
        self.fgcolor.placeholder_rule_id = self.fgcolor.bind('<Button-1>', GUI.removeplaceholder )
        self.fgcolor.root = self


        # Button
        self.generate = TkinterCustomButton.TkinterCustomButton(master=self,
                                            bg_color=None,
                                            fg_color=self.cget("bg"),
                                            border_color="#363945",
                                            hover_color="#798EA4",
                                            text_font=None,
                                            text="Generate",
                                            text_color="#363945",
                                            corner_radius=0,
                                            border_width=2,
                                            width=100,
                                            height=30,
                                            hover=True,
                                            command=self.generate)
        self.layout.create_window(75, 265+30, window=self.generate)                                         
        # Creduts and version
        self.credits = tkinter.Label(self, justify="center", bd=0, bg="#363945", fg="white", text="Created by DoktorSAS", font=("Terminal", 8))
        self.layout.create_window(75, 345, window=self.credits)  

        self.version = tkinter.Label(self, justify="center", bd=0, bg="#363945", fg="white", text="V 0.0.1", font=("Terminal", 7))
        self.layout.create_window(75, 325, window=self.version)  


        self.layout.pack(expand=1, fill="both")

         