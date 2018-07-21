#!/usr/bin/python

import Tkinter as tk
import AppKit
import subprocess
import sys

"""
This is a work in progress and an attempt to learn how to manage linx nodes remotely using python.
Change the node names to match your environment.
"""

class App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()
        self.master.title("Server Manager")
        self.master.resizable(False, False)
        self.master.tk_setPalette(background='#ececec')

        self.master.protocol('WM_DELETE_WINDOW', self.click_cancel)
        self.master.bind('<Return>', self.click_reset)
        self.master.bind('<Escape>', self.click_cancel)

        x = (self.master.winfo_screenwidth() - self.master.winfo_reqwidth()) / 2
        y = (self.master.winfo_screenheight() - self.master.winfo_reqheight()) / 3
        self.master.geometry("+{}+{}".format(x, y))

        self.master.config(menu=tk.Menu(self.master))

        self.svr_list = []

        self.status_msg = tk.StringVar()

        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.var5 = tk.IntVar()
        self.var6 = tk.IntVar()
        self.var7 = tk.IntVar()
        self.var8 = tk.IntVar()
        self.var1.set(0)
        self.var2.set(0)
        self.var3.set(0)
        self.var4.set(0)
        self.var5.set(0)
        self.var6.set(0)
        self.var7.set(0)
        self.var8.set(0)

        # tk.Message(self, text="Please enter a serial number or computer name to search for.\nClick Local to search for the local computer.",
        #    font='System 14 bold', justify='left', aspect=800).pack(pady=(15, 0))

        dialog_frame = tk.Frame(self)
        dialog_frame.pack(padx=20, pady=15)

        tk.Label(dialog_frame, text="Select the servers to manage.").pack()

        tk.Checkbutton(dialog_frame, text='MYNODE0', variable=self.var1, command=self.sel_110).pack(side='left')

        tk.Checkbutton(dialog_frame, text='MYNODE1', variable=self.var2, command=self.sel_111).pack(side='left')

        tk.Checkbutton(dialog_frame, text='MYNODE2', variable=self.var3, command=self.sel_112).pack(side='left')

        tk.Checkbutton(dialog_frame, text='MYNODE3', variable=self.var4, command=self.sel_113).pack(side='left')

        tk.Checkbutton(dialog_frame, text='MYNODE4', variable=self.var5, command=self.sel_114).pack(side='left')

        tk.Checkbutton(dialog_frame, text='MYNODE5', variable=self.var6, command=self.sel_115).pack(side='left')

        tk.Checkbutton(dialog_frame, text='MYNODE6', variable=self.var7, command=self.sel_116).pack(side='left')

        tk.Checkbutton(dialog_frame, text='MYNODE7', variable=self.var8, command=self.sel_117).pack(side='left')

        button_frame = tk.Frame(self)
        button_frame.pack(padx=5, pady=(0, 5), anchor='e')

        #self.clicked=[]
        button1 = tk.Button(button_frame, text="Status", width=8)
        button2 = tk.Button(button_frame, text="Start", width=8)
        button3 = tk.Button(button_frame, text="Stop", width=8)
        button4 = tk.Button(button_frame, text="Restart", width=8)
        button5 = tk.Button(button_frame, text="Reset", width=8)
        button6 = tk.Button(button_frame, text="Cancel", width=8)

        button1.pack(side='right')
        button2.pack(side='right')
        button3.pack(side='right')
        button4.pack(side='right')
        button5.pack(side='right')
        button6.pack(side='right')

        button1.configure(default='active', command=lambda btn=button1: self.run_Command(btn))
        button2.configure(command=lambda btn=button2: self.run_Command(btn))
        button3.configure(command=lambda btn=button3: self.run_Command(btn))
        button4.configure(command=lambda btn=button4: self.run_Command(btn))
        button5.configure(command=lambda btn=button5: self.click_reset(btn))
        button6.configure(command=lambda btn=button6: self.click_cancel(btn))


    def click_reset(self, event=None):
        self.var1.set(0)
        self.var2.set(0)
        self.var3.set(0)
        self.var4.set(0)
        self.var5.set(0)
        self.var6.set(0)
        self.var7.set(0)
        self.var8.set(0)

        self.svr_list = []

    def click_cancel(self, event=None):
        print("The user clicked 'Cancel'")
        self.master.destroy()

    def sel_110(self, event=None):
        #print("The user selected 110")
        sel_110_ck = self.var1.get()
        if sel_110_ck == 1:
            self.svr_list.append('MYNODE0.myschool.net')
        elif sel_110_ck == 0:
            self.svr_list.remove('MYNODE0.myschool.net')
        #print(self.svr_list)

    def sel_111(self, event=None):
        #print("The user selected 111")
        sel_111_ck = self.var2.get()
        if sel_111_ck == 1:
            self.svr_list.append('MYNODE1.myschool.net')
        elif sel_111_ck == 0:
            self.svr_list.remove('MYNODE1.myschool.net')
        #print(self.svr_list)

    def sel_112(self, event=None):
        #print("The user selected 112")
        sel_112_ck = self.var3.get()
        if sel_112_ck == 1:
            self.svr_list.append('MYNODE2.myschool.net')
        elif sel_112_ck == 0:
            self.svr_list.remove('MYNODE2.myschool.net')
        #print(self.svr_list)

    def sel_113(self, event=None):
        #print("The user selected 113")
        sel_113_ck = self.var4.get()
        if sel_113_ck == 1:
            self.svr_list.append('MYNODE3.myschool.net')
        elif sel_113_ck == 0:
            self.svr_list.remove('MYNODE3.myschool.net')
        #print(self.svr_list)

    def sel_114(self, event=None):
        #print("The user selected 114")
        sel_114_ck = self.var5.get()
        if sel_114_ck == 1:
            self.svr_list.append('MYNODE4.myschool.net')
        elif sel_114_ck == 0:
            self.svr_list.remove('MYNODE4.myschool.net')
        #print(self.svr_list)

    def sel_115(self, event=None):
        #print("The user selected 115")
        sel_115_ck = self.var6.get()
        if sel_115_ck == 1:
            self.svr_list.append('MYNODE5.myschool.net')
        elif sel_115_ck == 0:
            self.svr_list.remove('MYNODE5.myschool.net')
        #print(self.svr_list)

    def sel_116(self, event=None):
        #print("The user selected 116")
        sel_116_ck = self.var7.get()
        if sel_116_ck == 1:
            self.svr_list.append('MYNODE6.myschool.net')
        elif sel_116_ck == 0:
            self.svr_list.remove('MYNODE6.myschool.net')
        #print(self.svr_list)

    def sel_117(self, event=None):
        #print("The user selected 117")
        sel_117_ck = self.var8.get()
        if sel_117_ck == 1:
            self.svr_list.append('MYNODE7.myschool.net')
        elif sel_117_ck == 0:
            self.svr_list.remove('MYNODE7.myschool.net')
        #print(self.svr_list)

    def run_Command(self, btn):

        text = btn.cget("text")
        #self.clicked.append(text)
        #print "clicked:", self.clicked

        if text == "Status":
            COMMAND="systemctl status jamf.tomcat8 --no-pager | grep Active: | awk '{print $3}' | tr -d '()' | tr -d '\n'"

        if len(self.svr_list) != 0:
            self.svr_list.sort()
            for HOST in self.svr_list:

                ssh = subprocess.Popen(["ssh", "-t", "%s" % HOST, COMMAND],
                                       shell=False,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
                result = ssh.stdout.readlines()
                if result == []:
                    error = ssh.stderr.readlines()
                    print >>sys.stderr, "ERROR: %s" % error
                else:
                    #print HOST, " is ", result
                    self.status_msg = str(HOST) + " is " + str(result).strip('[]').strip("''")

                    message_frame = tk.Frame(self)
                    message_frame.pack()

                    stat_mg = tk.Label(message_frame, text=self.status_msg, justify='left').pack(pady=(1, 1))

            #self.click_reset(event)



if __name__ == '__main__':
    info = AppKit.NSBundle.mainBundle().infoDictionary()
    info['LSUIElement'] = True

    root = tk.Tk()
    app = App(root)
    AppKit.NSApplication.sharedApplication().activateIgnoringOtherApps_(True)
    app.mainloop()

"""
There are a few items left to address before we have a working GUI that matches the standard macOS dialogs. When running
a Python app using Tkinter the Python launcher's icon will appear in the Dock. This can be dynamically flagged to run
without the Dock icon by loading and manupulating the launcher's 'Info.plist' before the main window has been created.
'AppKit' will be used in our main function to do this.

Lastly, to allow the user to control the window as they would any other macOS dialog, we will bind the '<Return>' and
'<Escape>' keys to our 'OK' and 'Cancel' methods. We will also override the function of the close button on the GUI
window to point to our 'Cancel' method to keep control of the teardown.

Because we are now using alternative triggers for these funtions we must add an 'event' parameter to accept the callback
that is passed by the binding. The default value is set to 'None' for when the buttons are used.
"""
