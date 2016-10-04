#!/usr/bin/env python2
from psychopy import visual, core

win = visual.Window()
rect = visual.Rect(win)
rect.draw()
win.flip()
core.wait(1)
