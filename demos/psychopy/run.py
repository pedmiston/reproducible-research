#!/usr/bin/env python2
from psychopy import visual, core, sound, event
from pprint import pprint

from dynamic_mask import DynamicMask

# Trial settings
QUESTION_DURATION = 2.0
PAUSE_DURATION = 1.0
MASK_REFRESH_RATE = 0.01
TIMEOUT_DURATION = 2.0
keyboard_keys = dict(y='yes', n='no')

# Trial variables. Usually get from a csv.
question_text = 'Does it have big teeth?'
word_wav = 'stimuli/alligator.wav'
correct_answer = 'yes'

# Make trial objects
win = visual.Window()
question = visual.TextStim(win, question_text)
word = sound.Sound(word_wav)
mask = DynamicMask(win)
feedback = {0: sound.Sound("stimuli/buzz.wav"),
            1: sound.Sound("stimuli/bleep.wav")}
stopwatch = core.Clock()
WORD_DURATION = word.getDuration()

# Start trial
question.draw()
win.flip()
core.wait(QUESTION_DURATION)
win.flip()   # clears the screen during pause
core.wait(PAUSE_DURATION)
word.play()  # runs in background; does not wait
stopwatch.reset()  # start the timer at word onset
while stopwatch.getTime() < TIMEOUT_DURATION:
    response = event.getKeys(keyList=keyboard_keys.keys(),
                             timeStamped=stopwatch)
    if response:
        win.flip()
        break

    mask.draw()
    win.flip()
    core.wait(MASK_REFRESH_RATE)

key, rt = response[0] if response else ('NONE', TIMEOUT_DURATION * 1000)
response = keyboard_keys.get(key, key)
is_correct = int(response == correct_answer)
feedback[is_correct].play()

trial_data = dict(
    question=question_text,
    word=word_wav,
    correct_answer=correct_answer,
    key=key,
    response=response,
    rt=rt * 1000,  # clock times in ms
    is_correct=is_correct
)

pprint(trial_data)
