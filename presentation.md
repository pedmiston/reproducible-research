# Reproducible research with python
Pierce Edmiston  
pedmiston@wisc.edu  
github.com/pedmiston

# How I use python

- **running cognitive psychology experiments** on the influence of language on vision and human cognition more broadly (psychopy).
- **running behavioral experiments online** to test questions about the evolution of language (django).
- **doing data science** to glue everything above together (invoke).
- **mining the revision histories of Wikipedia articles** to understand the evolution of article quality (pywikibot, wikischolar).

# How I don't use python

- statistics, modeling, and data visualization (R)
- in groups

# psychopy

I use psychopy to run cognitive psychology experiments on the influence of language on vision and human cognition more broadly (psychopy).

- <http://www.psychopy.org/>
- [API](http://www.psychopy.org/api/api.html)
- [Install](http://www.psychopy.org/installation.html#manual-install)

## Installation

> I can only figure out how to run psychopy using 32-bit python2.7 installed with Canopy.

### Hurdle #1: scientific python

psychopy needs much of the sci-py stack (numpy, scipy, matplotlib), which can be tricky. The solution seems to be to download one of the python environments with the necessary dependencies, like [Canopy](https://www.enthought.com/products/canopy/) or [Anaconda](https://www.continuum.io/downloads).

### Hurdle #2: sound

psychopy needs either [pygame](http://www.pygame.org/hifi.html) or [pyo](http://ajaxsoundstudio.com/software/pyo/) to play sounds, neither of which are supported by Anaconda or Canopy. I haven't had any luck installing pyo from source, although it should be as easy as:

    pip install git+git://github.com/belangeo/pyo.git

Installing from a [binary](http://ajaxsoundstudio.com/software/pyo/) works, but on macOS it installs to a Framework build of python, so the files have to be moved. dylibs seem to be put in the right place.

### Demo

- Sample trials from a cognitive psychology experiment [here](/psychopy/)
- Full experiment: <https://github.com/lupyanlab/property-verification>
- Paper: <http://sapir.psych.wisc.edu/papers/edmiston_lupyan_JML.pdf>

# django

I use django for running large scale online experiments on the evolution of language.

## Frameworks are not for custom experiments

A partial list of the things I have to do when running an experiment as a webapp that are difficult to do using Django:

- Having forms where the choice labels are obscured.
- Are research participants users?

## But data modeling is amazing

Before django (before using a database!), my data was either heavily duplicated or held together by partial matches. It was incredibly error prone. Now I have enforced unique identifiers and foreign keys, so my tables are much thinner and my data is cleaner.

## However, there are much easier ways

- NoSQL maps much more closely onto my experimental process.
- Anything interactive requires front end work that django just isn't built for.

## That being said, I'm doing another one

I'm worried about the **second-system effect**.

## Demo

- [django app](https://github.com/lupyanlab/telephone)
- [infrastructure](https://github.com/lupyanlab/telephone-app)
- [live app](https://telephone.evoapps.xyz)
- [talk](http://sapir.psych.wisc.edu/evolang/fidelity.html#/)
- [media](http://www.sciencemag.org/news/2016/03/buzz-thwack-how-sounds-become-words)

# invoke

Reproducibility is an obsession for making everything repeatable easily.

- make
- rake
- drake
- invoke

## Demo

Scraping Kaggle competition leaderboards.

# pywikibot and wikischolar

I'm interested in understanding how Wikipedia article quality changes over time. This requires fetching old versions of Wikipedia articles and evaluating their quality in some way.

pywikibot is a python package for making Wikipedia bots. They connect with MediaWiki servers, query data, make changes, and post the changes as edits. More and more of the work being done on Wikipedia is being automated.

The WMF also exposes a few APIs that help to automate the tasks of vigilant Wikipedia editors all over the world. One is called the "Objective Revision Evaluation Service" and is used to generate predictions about article quality given only a revision id.

wikischolar is a python package built on top of pywikibot that fetches historical versions of articles and (among other things) calculates their predicted article quality using the ORES APIs.
