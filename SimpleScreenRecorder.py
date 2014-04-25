#!/usr/bin/env python

"""
A Simple Screen Capture Utility , utilizes avconv with H264 support
By default it captures the entire desktop.

Requirements
install libraries
sudo apt-get install wget libav-tools ffmpeg libavc1394-0 libavformat-extra-53 libavfilter2 libavutil-extra-51 mencoder libavahi-common-data

"""

################################ LICENSE BLOCK ################################
# Copyright (c) 2011 Abhishek Jaiswal
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
###############################################################################

from Tkinter import *
from threading import Thread
from os.path import expanduser
import os
import time
import datetime
import tkFont


class ScreenRecorder():

    root = Tk()
    btn_rec = None
    btn_stop = None
    lbl_time = None
    timer_flag = 1


    def __init__(self):
        pass

    def main_function(self):

        font_time = tkFont.Font(family="Helvetica", size=12)
        font_button = tkFont.Font(family="Monospace", size=11,weight="bold")

        self.lbl_time = Label(self.root, text="00m:00s", fg="blue", font="fontTime")

        self.btn_rec = Button(self.root, text="Record", command=self.rec, state=ACTIVE, font="fontButton")
        self.btn_stop = Button(self.root, text=" Stop ", command=self.stop, state=DISABLED, font="fontButton")

        l = Label(self.root, text="test 1")
        l1 = Label(self.root, text="text 2")
        l2 = Label(self.root, text="text 3")
        text = Text(self.root, height=2, width=25)

        self.lbl_time.grid(row=0, column=0, columnspan=2)

        self.btn_rec.grid(row=1, column=0, padx=1, pady=5)
        self.btn_stop.grid(row=1, column=1, padx=1)
        l.grid(row=2, column=0,columnspan=2)
        l1.grid(row=3, column=0,columnspan=2)
        l2.grid(row=4, column=0,columnspan=2)
        text.grid(row=4, column=0,columnspan=2)
        self.root.minsize(160,105)
        self.root.maxsize(400,400)
        self.root.title("Desktop REC")
        self.root.attributes("-topmost", 1)
        self.root.mainloop()

    def rec(self):
        print "here in rec"

        self.btn_rec.config(state=DISABLED)
        self.btn_stop.config(state=ACTIVE)
        self.timer()

    def stop(self):
        print "here in stop"
        self.btn_stop.config(state=DISABLED)
        self.btn_rec.config(state=ACTIVE)
        self.timer_flag = 0

    def timer(self):
        mins = 0
        secs = 0

        while True:

            if not self.timer_flag:
                print "not start"
                break

            else:
                self.lbl_time['text'] = str("%02dm:%02ds" % (mins, secs))

                if secs == 0:
                    time.sleep(0)

                else:
                    time.sleep(1)

                if secs == 60:
                    secs = 0
                    mins += 1
                    self.lbl_time['text'] = str("%02dm:%02ds" % (mins, secs))

                self.root.update()
                secs += 1


s = ScreenRecorder()
s.main_function()