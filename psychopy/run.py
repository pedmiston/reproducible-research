#!/usr/bin/env python2
from psychopy import visual, core, sound, event
from pprint import pprint

# Trial settings
QUESTION_DURATION = 2.0
PAUSE_DURATION = 1.0
TIMEOUT_DURATION = 2.0
keyboard_keys = dict(y='yes', n='no')

# Trial variables. Usually get from a csv.
question_txt = 'Does it have big teeth?'
word_wav = 'stimuli/alligator.wav'
correct_answer = 'yes'

# Make trial objects
win = visual.Window()
question = visual.TextStim(win, question_txt)
word = sound.Sound(word_wav)
feedback = {0: sound.Sound("stimuli/bleep.wav"),
            1: sound.Sound("stimuli/buzz.wav")}
stopwatch = core.Clock()

# Start trial
question.draw()
win.flip()
core.wait(QUESTION_DURATION)
core.wait(PAUSE_DURATION)
word.play()  # runs in background; does not wait
stopwatch.reset()
core.wait(word.getDuration())
response = event.waitKeys(keyList=keyboard_keys.keys(),
                          maxWait=TIMEOUT_DURATION,
                          timer=stopwatch)

key, rt = response[0] if response else ('NONE', TIMEOUT_DURATION * 1000)
response = keyboard_keys[key]
is_correct = (response == correct_answer)
feedback[is_correct].play()

trial_data = dict(
    question_txt=question_text,
    word_wav=word_wav,
    correct_answer=correct_answer,
    key=key,
    response=response,
    rt=rt * 1000,  # clock times in ms
    is_correct=is_correct
)

pprint(trial_data)
