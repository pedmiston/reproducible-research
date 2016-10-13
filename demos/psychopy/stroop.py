from psychopy import visual, core, event

instructions = "Press the key for the first letter of the color the word is " +\
               "printed in (not the first letter of the word)."

win = visual.Window(fullscr=True)
header = visual.TextStim(win, instructions, pos=[0,0.4], color="black")
stimulus = visual.TextStim(win)

trials = [
    ('orange', 'orange'),
    ('green', 'red'),
    ('blue', 'green'),
    ('red', 'red'),
]

def run_trial(name, color):
    stimulus.setText(name)
    stimulus.setColor(color)

    header.draw()
    stimulus.draw()
    win.flip()
    response = event.waitKeys(keyList=list('roygb'))

    key = response[0]
    is_correct = int(key == color[:1])
    print name, color, key, is_correct

for trial in trials:
    run_trial(*trial)
    win.flip()
    core.wait(1)
