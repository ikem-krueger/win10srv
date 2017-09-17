#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Sep 13, 2017 02:11:24 AM
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
    top = New_Toplevel_1 (root)
    win10srv_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel_1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel_1 (w)
    win10srv_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None


class New_Toplevel_1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('vista')

        top.geometry("270x166+428+169")
        top.title("Windows 10 Service Repair")
        top.resizable(width=False, height=False)
        top.bind('<Escape>', lambda e:top.destroy())


        self.TLabel1 = ttk.Label(top)
        self.TLabel1.place(relx=0.04, rely=0.06, height=19, width=44)
        self.TLabel1.configure(text='''Service:''')

        self.TLabel2 = ttk.Label(top)
        self.TLabel2.place(relx=0.24, rely=0.06, height=19, width=160)
        self.TLabel2.configure(text='''-''')

        self.TLabel3 = ttk.Label(top)
        self.TLabel3.place(relx=0.04, rely=0.18, height=19, width=39)
        self.TLabel3.configure(text='''Status:''')

        self.TLabel4 = ttk.Label(top)
        self.TLabel4.place(relx=0.24, rely=0.18, height=19, width=160)
        self.TLabel4.configure(text='''-''')

        self.TLabel5 = ttk.Label(top)
        self.TLabel5.place(relx=0.04, rely=0.3, height=19, width=48)
        self.TLabel5.configure(text='''Success:''')

        self.TLabel6 = ttk.Label(top)
        self.TLabel6.place(relx=0.24, rely=0.3, height=19, width=160)
        self.TLabel6.configure(text='''0''')

        self.TLabel7 = ttk.Label(top)
        self.TLabel7.place(relx=0.04, rely=0.42, height=19, width=42)
        self.TLabel7.configure(text='''Failure:''')

        self.TLabel8 = ttk.Label(top)
        self.TLabel8.place(relx=0.24, rely=0.42, height=19, width=160)
        self.TLabel8.configure(text='''0''')

        self.TProgressbar1 = ttk.Progressbar(top)
        self.TProgressbar1.place(relx=0.04, rely=0.6, relwidth=0.9
                , relheight=0.0, height=22)
        self.TProgressbar1.configure(length="250")

        self.TButton1 = ttk.Button(top)
        self.TButton1.place(relx=0.04, rely=0.78, height=25, width=76)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''About''')
        self.TButton1.configure(underline="0")
        self.TButton1.bind('<Button-1>',lambda e:win10srv_support.show_about_dialog(e))
        self.TButton1.bind('<Return>',lambda e:win10srv_support.show_about_dialog(e))
        self.TButton1.bind('<space>',lambda e:win10srv_support.show_about_dialog(e))
        top.bind('<Alt-a>',lambda e:win10srv_support.show_about_dialog(e))

        self.TButton2 = ttk.Button(top)
        self.TButton2.place(relx=0.37, rely=0.78, height=25, width=76)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''Log''')
        self.TButton2.configure(underline="0")
        self.TButton2.configure(state=DISABLED)

        self.TButton3 = ttk.Button(top)
        self.TButton3.place(relx=0.67, rely=0.78, height=25, width=76)
        self.TButton3.configure(takefocus="")
        self.TButton3.configure(text='''Repair''')
        self.TButton3.configure(underline="0")
        self.TButton3.bind('<Button-1>',lambda e:win10srv_support.repair_windows_services(e))
        self.TButton3.bind('<Return>',lambda e:win10srv_support.repair_windows_services(e))
        self.TButton3.bind('<space>',lambda e:win10srv_support.repair_windows_services(e))
        top.bind('<Alt-r>',lambda e:win10srv_support.repair_windows_services(e))
        self.TButton3.focus()





if __name__ == '__main__':
    if ctypes.windll.shell32.IsUserAnAdmin():
        vp_start_gui()
    else:
        hinstance = ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, sys.argv[0], None, 0)

        if hinstance <= 32:
            sys.exit(1)

