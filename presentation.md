# Reproducible research with python
Pierce Edmiston  
<pedmiston@wisc.edu>  
[github.com/pedmiston](https://github.com/pedmiston)

# How I use python

**Cognitive psychology experiments**
: on the influence of language on human cognition.

**Behavioral psychology experiments**
: to test questions about the evolution of language.

**Mining Wikipedia article revision histories**
: to understand the evolution of article quality.

**Basic data science**
: to glue everything above together.

# ! (How I use python)

- I don't use python for statistics, modeling, and visualization.  
- Most of the code I write only I ever read.

# Reproducibility

> A tale of two computers.

Reproducibility is an **obsession** for making everything able to be repeated and easily repeatable.

# psychopy

##

[![](http://www.psychopy.org/_static/psychopyDocBanner2.gif)](http://www.psychopy.org)

## Hello world!

```python
from psychopy import visual, core
win = visual.Window(fullsrc=True)
text = visual.TextStim(win, "Hello world!")
text.draw()
win.flip()
core.wait(1)
core.quit()
```

## Stroop task

```python
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
```

<small>[Wikipedia: The Stroop effect](https://en.wikipedia.org/wiki/Stroop_effect)</small>

## Links

- [Package API](http://www.psychopy.org/api/api.html)
- [Installation instructions](http://www.psychopy.org/installation.html#manual-install)

## Installations, I've had a few

- ~~Standard python2 install.~~
- ~~Anaconda environment with python2~~
- **Canopy install with python2**

## Hurdle #1: scientific python

`psychopy` needs much of the sci-py stack (`numpy`, `scipy`, `matplotlib`). Download one of the python environments that bundles the necessary dependencies:

- [Enthought Canopy](https://www.enthought.com/products/canopy/)
- [Continuum Anaconda](https://www.continuum.io/downloads)

## Hurdle #2: sound

`psychopy` needs either `pygame` or `pyo` to play sounds, neither of which are supported by Anaconda or Canopy.

- `pip install git+git://github.com/belangeo/pyo.git`
- Install from a [binary](http://ajaxsoundstudio.com/software/pyo/)[^1]

[^1]: On macOS it installs to a Framework build of `python`, so the files have to be moved. The sound `dylibs` seem to be put in the right place.

## Demo

- Sample trial from a cognitive psychology experiment [here](https://github.com/pedmiston/reproducible-research/demos/psychopy/run.py).
- Full experiment: [property-verification](https://github.com/lupyanlab/property-verification/experiment).
- Paper ([pdf](http://sapir.psych.wisc.edu/papers/edmiston_lupyan_JML.pdf)).

# django

##

> Let's run experiments on the web.

- Artificial music marketplace ([Salganik, Dodds, & Watts, 2006](http://www.princeton.edu/~mjs3/salganik_dodds_watts06_full.pdf))
- Run a huge version of the children's game of telephone on the web.

## Telephone

1. Listen to a recording, record a response.
2. Validate recordings as they come in.
3. Run different surveys on the imitations.

## Lessons learned

- Frameworks are not for custom experiments.
- But data modeling is amazing.
- However, there are much easier ways (NoSQL, Flask).
- That said, I'm doing another one in Django.

<small>[Wikipedia: Second-system effect](https://en.wikipedia.org/wiki/Second-system_effect)</small>

## Demo

- [Django app](https://github.com/lupyanlab/telephone)
- [Ansible infrastructure](https://github.com/lupyanlab/telephone-app)
- [Live app](https://telephone.evoapps.xyz)
- [Conference talk](http://sapir.psych.wisc.edu/evolang/fidelity.html#/)
- [Media coverage](http://www.sciencemag.org/news/2016/03/buzz-thwack-how-sounds-become-words)

# invoke

## Glue for raw data

- Behavioral data (.txt)
- Eyetracking data (.hdf5)
- Web survey data (Qualtrics, MTurk)
- RDBMS + media files (Telephone)
- other web queries (Wikipedia)

## Many options for reproducible data workflows

- make (Makefile)
- rake (Rakefile)
- drake (Drakefile)
- bash (\*)
- invoke (tasks.py)

## Hello world!

```bash
$ cat tasks.py
```

```python
from invoke import task

@task
def hello(ctx):
    ctx.run("echo Hello World!")
```

```bash
$ invoke hello
Hello World!
```

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

```bash
$ cat user-config.py
family = 'wikipedia'
mylang = 'en'
```

```python
>>> import pywikibot
>>> site = pywikibot.Site('en', 'wikipedia')
>>> page = pywikibot.Page(site, 'Splendid_fairywren')
>>> page.get()  # Wikipedia page text in mediawiki format
```

## Demo

- Simple Wikipedia revision downloader with `pywikibot` and `invoke` [here](https://github.com/pedmiston/reproducible-research/demos/pywikibot)
- Wikischolar demo [here](https://github.com/pedmiston/reproducible-research/demos/wikischolar)
