# Reproducible research workflows in python

Python's literate syntax makes it a great tool for tying together the random parts of a typical research project into a reproducible workflow. I'll talk about some of the strategies and tools that I've found useful for conducting reproducible research. Reproducible research is an important component of open science, and involves being able to recreate whatever conditions were necessary to observe an effect of interest. Today, the most practical form of reproducibility is documenting the steps of a research project as much as possible in code. Python makes it easy.

## Python packages

Here are some of the python packages I'll be talking about.

- [invoke](http://www.pyinvoke.org/)
- [psychopy](http://www.psychopy.org/)
- [pandas](http://pandas.pydata.org/)
- [pywikibot](https://www.mediawiki.org/wiki/Manual:Pywikibot) and other Wikipedia tools

## Projects

For real world examples, I'll be referring to a few of my research projects.

- [property-verification](https://github.com/lupyanlab/property-verification/). A reproducible cognitive psychology experiment.
- [wikischolar](https://github.com/evoapps/wikischolar/). A data science project investigating the evolution of Wikipedia articles.
- [diachronic-teams](https://github.com/pedmiston/diachronic-teams/). A research project involving invoke tasks for scraping data from Kaggle leaderboards.

## Using this repo

To build the presentation, clone it, and use pandoc to convert "presentation.md" to "presentation.html". To make things easier, I include the reveal.js
repo as a submodule. Actually, it's my personal fork of the reveal.js repo, the only difference between it and it's upstream branch is that my version ignores the "index.html" file so that when I build **this** presentation, I can just output the pandoc results as "index.html" in the revealjs submodule, and I don't have to worry about any modifications clogging up my git status.

    git clone https://github.com/pedmiston/reproducible-research
    cd reproducible-research
    git submodule init
    git submodule update
    ./build
    open presentation.html

## General notes

I make heavy use of `git submodules` and virtualenv's, using `virtualenvwrapper` as much as possible.
