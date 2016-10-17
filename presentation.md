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

<small>[Wikipedia: The Stroop effect](https://en.wikipedia.org/wiki/Stroop_effect)</small>

```python
from psychopy import visual, event
instructions = "Press the key for the first letter of the color the word" +\
               "is printed in (not the first letter of the word)."
name, color = 'green', 'red'
win = visual.Window(fullscr=True)
header = visual.TextStim(win, instructions, pos=[0,0.4])
stimulus = visual.TextStim(win, name, color=color)
header.draw()
stimulus.draw()
win.flip()
response = event.waitKeys(keyList=list('roygbiv'))
```

## Links

- [Package API](http://www.psychopy.org/api/api.html)
- [Installation instructions](http://www.psychopy.org/installation.html#manual-install)

## Installations, I've had a few

- ~~Standard python2 install.~~
- ~~Anaconda environment with python2~~
- **Canopy install with 32-bit python2**

## Hurdle #1: scientific python

`psychopy` needs much of the sci-py stack (`numpy`, `scipy`, `matplotlib`). Download one of the python environments that bundles the necessary dependencies:

- [Enthought Canopy](https://www.enthought.com/products/canopy/)
- [Continuum Anaconda](https://www.continuum.io/downloads)

## Hurdle #2: sound

`psychopy` needs either `pygame` or `pyo` to play sounds, neither of which are supported by Anaconda or Canopy.

- `pip install git+git://github.com/belangeo/pyo.git#egg=Pyo`
- Install from a [binary](http://ajaxsoundstudio.com/software/pyo/)

## Demo

- Sample trial from a cognitive psychology experiment [here](https://github.com/pedmiston/reproducible-research/blob/master/demos/psychopy/property_verification.py).
- Full experiment: [property-verification](https://github.com/lupyanlab/property-verification/tree/master/experiment).

# django

##

Let's run experiments on the web!

- Artificial music marketplace ([Salganik, Dodds, & Watts, 2006](http://www.princeton.edu/~mjs3/salganik_dodds_watts06_full.pdf))
- Run a huge version of the children's game of telephone on the web.

## Telephone

1. Get a message, record a response.
2. Validate recordings as they come in.
3. Run different surveys on the imitations.

## Lessons learned

- Frameworks are not for custom experiments.
- But data modeling is great.
- However, there are much easier ways (NoSQL, Flask).
- That said, I'm doing another one in Django.

<small>[Wikipedia: Second-system effect](https://en.wikipedia.org/wiki/Second-system_effect)</small>

## Demo

- [Django app](https://github.com/lupyanlab/telephone)
- [Ansible infrastructure](https://github.com/lupyanlab/telephone-app)
- [Live app](https://telephone.evoapps.xyz)

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
- invoke (tasks.py)

+ bash, sed, awk

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
$ invoke hello  # or just `inv hello`
Hello World!
```

## Links

- [Read the Docs](http://docs.pyinvoke.org/en/latest/index.html)
- [Getting started](http://docs.pyinvoke.org/en/latest/getting_started.html)

## Demo

Write an `invoke` task for getting a Wikipedia article's revision history using `pywikibot`.

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

## As an invoke task

```python
@task
def get(ctx, title, n_revisions=10, content=False, output_csv=None):
    """Get the last n revisions of a Wikipedia article by title."""
    site = pywikibot.Site('en', 'wikipedia')
    page = pywikibot.Page(site, title)
    revisions = page.revisions(content=content)
    records = [next(revisions).__dict__ for _ in range(n_revisions)]
    table = pandas.DataFrame.from_records(records)
    table.insert(0, 'title', title)
    table.to_csv(output or sys.stdout, index=False)
```

```bash
$ inv get "Splendid fairywren" -n 100 -o splendid_fairywren.csv
```

# invoke as a library

## wikischolar

`wikischolar` is a python package for studying Wikipedia article revision histories.

## Wikipedia articles about Wikipedia articles

My goal was to allow people to research with `wikischolar` all of the Wikipedia articles on a particular list article.

- [Lists of lists of lists](https://en.wikipedia.org/wiki/List_of_lists_of_lists)
- Ex: [Current US Senators](List_of_current_United_States_Senators)

A script for parsing a Wikipedia List article into a csv of article titles for consumption by `wikischolar` is available [here](https://github.com/evoapps/wikischolar/blob/master/bin/senators.py).

## setup.py

```python
from distutils.core import setup

setup(
    name='wikischolar',
    version='0.1.0',
    packages=['wikischolar'],
    install_requires=['invoke'],
    entry_points={
        'console_scripts': ['sch = wikischolar.main:program.run']
    },
)
```

## main.py

```python
from invoke import Program
from wikischolar.tasks import namespace

program = Program(version='0.1.0', namespace=namespace)
```

## tasks.py

```python
from invoke import task, Collection

# Functions decorated with @task:
# ...

namespace = Collection(
    load,
    dump,
    execute,
    revisions,
    qualities,
    edits,
    generations,
)
```

## Demo

Use `wikischolar` to get historical article quality data for a Wikipedia List article.
