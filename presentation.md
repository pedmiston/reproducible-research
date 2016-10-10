# Reproducible research with python
Pierce Edmiston  
<pedmiston@wisc.edu>  
[github.com/pedmiston](https://github.com/pedmiston)

# How I use python

**Cognitive psychology experiments**
: on the influence of language on vision and human cognition more broadly.

**Behavioral psychology experiments**
: to test questions about the evolution of language.

**Basic data science**
: to glue everything above together.

**Mining Wikipedia article revision histories**
: to understand the evolution of article quality.

# ! (How I use python)

- Statistics, modeling, and visualization.
- In groups.

# Reproducibility

> A tale of two computers.

Reproducibility is an **obsession** for making everything repeatable easily.

# psychopy

##

[![](http://www.psychopy.org/_static/psychopyDocBanner2.gif)](http://www.psychopy.org)

## Hello world!

    from psychopy import visual, core
    win = visual.Window(fullsrc=True)
    text = visual.TextStim(win, "Hello world!")
    text.draw()
    win.flip()
    core.wait(1)
    core.quit()

## Stroop task

    from psychopy import visual, core
    name, color = 'green', 'red'
    win = visual.Window(fullscr=True)
    instructions = "Press the key for the first letter of the color the " + \
                   "word is printed in (not the first letter of the word)."
    help = visual.TextStim(win, instructions, pos=[0,-20])
    stimulus = visual.TextStim(win, name, color=color)
    help.draw()
    stimulus.draw()
    win.flip()
    response = event.waitKeys(keyList=list('roygbiv'))

## Links

- [Package API](http://www.psychopy.org/api/api.html)
- [Installation instructions](http://www.psychopy.org/installation.html#manual-install)

## Installation methods, I've had a few

- ~~Standard python2 install.~~
- ~~Anaconda environment with python2~~
- **Canopy install with python2**

## Hurdle #1: scientific python

`psychopy` needs much of the sci-py stack (`numpy`, `scipy`, `matplotlib`), which can be tricky. The solution seems to be to download one of the python environments that bundles the necessary dependencies, like [Enthought Canopy](https://www.enthought.com/products/canopy/) or [Continuum Anaconda](https://www.continuum.io/downloads).

## Hurdle #2: sound

psychopy needs either [pygame](http://www.pygame.org/hifi.html) or [pyo](http://ajaxsoundstudio.com/software/pyo/) to play sounds, neither of which are supported by Anaconda or Canopy. I haven't had any luck installing pyo from source, although it should be as easy as:

    pip install git+git://github.com/belangeo/pyo.git

Installing from a [binary](http://ajaxsoundstudio.com/software/pyo/) works, but on macOS it installs to a Framework build of python, so the files have to be moved. The sound dylibs seem to be put in the right place.

## Demo

- Sample trial from a cognitive psychology experiment [here](https://github.com/pedmiston/reproducible-research/demos/psychopy).
- Full experiment: [property-verification](https://github.com/lupyanlab/property-verification).
- Paper ([pdf](http://sapir.psych.wisc.edu/papers/edmiston_lupyan_JML.pdf)).

# django

##

> Let's run experiments on the web.

- Existing solution using Qualtrics + Mechanical Turk.
- Example: Artificial music marketplace ([Salganik, Dodds, & Watts, 2006](http://www.princeton.edu/~mjs3/salganik_dodds_watts06_full.pdf))
- Run a huge game of telephone on the web.

## Telephone app

1. Click on a link, listen to a recording, and record a response.
2. Be able to validate the recordings as they come in.
3. Run different surveys on the imitations once they are gathered.

## Lessons learned

- Frameworks are not for custom experiments.
- But data modeling is amazing.
- However, there are much easier ways (NoSQL, Flask).
- That said, I'm doing another one in Django.

## Demo

- [django app](https://github.com/lupyanlab/telephone)
- [infrastructure](https://github.com/lupyanlab/telephone-app)
- [live app](https://telephone.evoapps.xyz)
- [talk](http://sapir.psych.wisc.edu/evolang/fidelity.html#/)
- [media](http://www.sciencemag.org/news/2016/03/buzz-thwack-how-sounds-become-words)

# invoke

## Raw data

- Behavioral data ("52 pickup" of plain text files)
- Eyetracking data (.hdf5)
- Web survey data (Qualtrics, MTurk)
- SQL data + media files (Telephone)
- other web queries

## Many options for reproducible data workflows

- make (Makefile)
- rake (Rakefile)
- drake (Drakefile)
- invoke (tasks.py)

## Hello world!

    $ cat tasks.py
    from invoke import task

    @task
    def hello(ctx):
        ctx.run("echo Hello World!")

    $ invoke hello
    Hello World!

## Links

- [Read the Docs](http://docs.pyinvoke.org/en/latest/index.html)
- [Getting started](http://docs.pyinvoke.org/en/latest/getting_started.html)

## Demo

- Messy, real world example: [words-in-transition](https://github.com/lupyanlab/words-in-transition)
- Awesome, but totally unnecessary example: [diachronic-teams](https://github.com/pedmiston/diachronic-teams)

# pywikibot and wikischolar

##

- `pywikibot` is a python package for making Wikipedia bots.
- The Wikimedia Foundation exposes machine learning algorithms trained to predict article quality.
- `wikischolar` is "a python package" for gathering historical article quality data.

## Hello Splendid fairywren!

    $ cat user-config.py
    family = 'wikipedia'
    mylang = 'en'

    >>> import pywikibot
    >>> site = pywikibot.Site('en', 'wikipedia')
    >>> page = pywikibot.Page(site, 'Splendid_fairywren')
    >>> page.get()

## Demo

- Simple Wikipedia revision downloader with `pywikibot` and `invoke` [here](https://github.com/pedmiston/reproducible-research/demos/pywikibot)
- Wikischolar demo [here](https://github.com/pedmiston/reproducible-research/demos/wikischolar)
