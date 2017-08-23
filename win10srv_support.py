#! /usr/bin/env python
#
# Support module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Jul 25, 2017 01:18:29 PM

import threading
from time import sleep
import os, sys
import re
import subprocess

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


def show_info_dialog(p1):
    print('show_info_dialog()')
    sys.stdout.flush()

# sc query type=service
# sc [start|stop] <service>

def update_progress_bar():
    path = "Windows 10 default services"

    reg_files = os.listdir(path)
    no_files = len(reg_files)

    reg_files_error = []
    success = 0
    failure = 0

    for file_no, reg_file in enumerate(reg_files):
        percent = (100*(file_no+1))//no_files

        service = re.subn("_", " ", reg_file)[0]
        service = re.subn("\.reg$", "", service)[0]

        w.Label2["text"] = service
        w.Label8["text"] = "Reset..."

        r_value = subprocess.call(["reg", "import", "%s/%s" % (path, reg_file)]) # reg import yourfile.reg

        if r_value == 0:
            w.Label8["text"] = "Done"

            success += 1
        else:
            failure += 1
            
            reg_files_error.append(reg_file)
        
        w.Label4["text"] = success
        w.Label6["text"] = failure

        print("%s%% %s %s" % (percent, service, r_value))
        
        w.TProgressbar1["value"] = percent

    #print(reg_files_error)

def repair_windows_services(p1):
    print('repair_service_files()')

    sys.stdout.flush()

    t = threading.Thread(target=update_progress_bar)
    t.start()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import win10srv
    win10srv.vp_start_gui()
