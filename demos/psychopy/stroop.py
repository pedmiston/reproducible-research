from psychopy import visual, core
instructions = "Press the key for the first letter of the color the word is printed in (not the first letter of the word)."
name, color = 'green', 'red'
win = visual.Window(fullscr=True)
header = visual.TextStim(win, instructions, pos=[0,-20])
stimulus = visual.TextStim(win, name, color=color)
header.draw()
stimulus.draw()
win.flip()
response = event.waitKeys(keyList=list('roygbiv'))