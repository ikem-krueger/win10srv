#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Jul 28, 2017 01:53:51 PM
import sys
import ctypes

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import win10srv_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Windows_10_Service_Repair (root)
    win10srv_support.init(root, top)
    root.mainloop()

w = None
def create_Windows_10_Service_Repair(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Windows_10_Service_Repair (w)
    win10srv_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Windows_10_Service_Repair():
    global w
    w.destroy()
    w = None


class Windows_10_Service_Repair:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("222x165+464+258")
        top.title("Windows 10 Service Repair")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.TProgressbar1 = ttk.Progressbar(top)
        self.TProgressbar1.place(relx=0.05, rely=0.61, relwidth=0.9
                , relheight=0.0, height=22)

        self.Label1 = Label(top)
        self.Label1.place(relx=0.05, rely=0.06, height=21, width=46)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor=W)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Service:''')

        self.Button1 = Button(top)
        self.Button1.place(relx=0.74, rely=0.79, height=24, width=44)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Repair''')
        self.Button1.configure(underline="0")
        self.Button1.bind('<Button-1>',lambda e:win10srv_support.repair_windows_services(e))

        self.Button3 = Button(top)
        self.Button3.place(relx=0.05, rely=0.79, height=24, width=32)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Info''')
        self.Button3.configure(underline="0")
        self.Button3.bind('<Button-1>',lambda e:win10srv_support.show_info_dialog(e))

        self.Label2 = Label(top)
        self.Label2.place(relx=0.27, rely=0.06, height=21, width=144)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor=W)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''None''')

        self.Label3 = Label(top)
        self.Label3.place(relx=0.05, rely=0.3, height=21, width=50)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Success:''')

        self.Label4 = Label(top)
        self.Label4.place(relx=0.27, rely=0.3, height=21, width=140)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(anchor=W)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''0''')

        self.Label5 = Label(top)
        self.Label5.place(relx=0.05, rely=0.42, height=21, width=44)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Failure:''')

        self.Label6 = Label(top)
        self.Label6.place(relx=0.27, rely=0.42, height=21, width=140)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(anchor=W)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''0''')

        self.Label7 = Label(top)
        self.Label7.place(relx=0.05, rely=0.18, height=21, width=41)
        self.Label7.configure(anchor=W)
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''Status:''')

        self.Label8 = Label(top)
        self.Label8.place(relx=0.27, rely=0.18, height=21, width=144)
        self.Label8.configure(anchor=W)
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(text='''None''')






if __name__ == '__main__':
    if ctypes.windll.shell32.IsUserAnAdmin():
        vp_start_gui()
    else:
        hinstance = ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, sys.argv[0], None, 0)

        if hinstance <= 32:
            sys.exit(1)


