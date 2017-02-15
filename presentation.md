---
title: Adopting open source practices<br/>for better science
author: |
  Pierce Edmiston  
  <pedmiston@wisc.edu>  
  [sapir.psych.wisc.edu](http://sapir.psych.wisc.edu)  
  [github.com/pedmiston](https://github.com/pedmiston)
output:
  xaringan::moon_reader:
    css: ["default", "static/font.css"]
---

# Outline

Open source practices that make for more reproducible science:

1. Version control
2. Dynamic documents
3. Building from source

Conclusion: It's worth it!



---
# Why I care about reproducibility

1. I want my research to be reproducible.
2. I want to attract collaborators.

???

I want my research to be reproducible by other people and by myself. This means no undocumented steps! Document things in code for maximum reproducibility.

I want the bar for getting involved in one of my projects to be as low as possible.

---
# The reproducibility crisis

<small>Open Science Collaboration. (2015). Estimating the reproducibility of psychological science. _Science_.</small>

<img src="presentation_files/figure-html/reproducibility-crisis-1.png" width="672" />

???

My interest in reproducibility is really more of an obsession or a paranoia. I worry that my own research is not going to replicate.

---
### Why isn't psychological research more reproducible?

- Simmons, Nelson, & Simonsohn. (2011). False-positive psychology. _Psychological Science_.
- Gelman & Loken. (2013). The garden of forking paths. Unpublished manuscript.
- Palmeri. (2016). Psychology is in crisis over whether it's in crisis. _WIRED_.
- Ioannidis. (2005). Why most published research findings are false. _PLOS Medicine_.
- Edmiston. (now). Publications are not answers to research questions. Unpublished thoughts.

???

The first reason is that there is a lot of flexibility in how we analyze behavioral data. The second reason is that we tend to look until we find something. But of course there are plenty of people who disagree whether the state of psychology research is as bad as some say. And actually these problems with publication bias and the file drawer effect are much more widespread than just psychology. Personally I think the culprit is the idea that publications are definitive answers to research questions.

---
# Reproducibility is a big problem

<small>Munafò et al. (2017). A manifesto for reproducible science. _Nature_.</small>

<img src="presentation_files/figure-html/threats-to-reproducibility-1.png" width="672" />

---
# Steps toward reproducible science

- Blind data analysts to experiment conditions.
- Improve statistics education (adapted for web).
- Hire methodological consultants.
- Seek collaboration for scalability.

---
# Why I think open source is the answer

Compare these two goals of reproducibility in science and in open source:

1. Fellow researchers should be able to reproduce my work.  
2. Anyone should be able to use and contribute to this project.

<!--html_preserve--><div id="htmlwidget-f61fb122792d2df61da2" style="width:672px;height:200px;" class="grViz html-widget"></div>
<script type="application/json" data-for="htmlwidget-f61fb122792d2df61da2">{"x":{"diagram":"\ndigraph {\n  label = \"Open source science\";\n  labelloc = t;\n  fontname = \"Helvetica-bold\";\n  node[shape = none, fontname = Helvetica];\n  Reproducibility -> {Confidence, Collaboration};\n}","config":{"engine":"dot","options":null}},"evals":[],"jsHooks":[]}</script><!--/html_preserve-->

???

Open source is the answer because the goal of reproducibility in open source communities is actually a loftier goal than in the scientific community.

---
class: center

# Version control


<img src="presentation_files/figure-html/version-control-in-the-wild-1.png" width="1152" />

---
# Pick your poison

- **git**
- mercurial
- subversion
- gitless

---
class: center

# Tools for climbing

<img src="presentation_files/figure-html/climbing-tools-1.png" width="672" />

???

There are a number of ways to think about version control. One way is to think about it as a safety net, that no matter what you do, you can always roll back to what it was before. This is the power of the "undo" button. However, this doesn't really get at why I think version control is such a powerful tool. A better analogy is to think about version control as a tool for climbing. The picture is of tools used by rock climbers called "nuts" that you jam into a crack in the rock, and then you can use it as a hold. This is how I think about version control. It definitely has the effect of keeping you safer, but it also allows you to climb in places you otherwise wouldn't be able to.

---
class: center

# Conquer clutter

<img src="presentation_files/figure-html/cluttered-folder-1.png" width="672" />

---
class: center

# Forks and branches

<!--html_preserve--><div id="htmlwidget-b726cd6f19709e90cb0f" style="width:672px;height:200px;" class="grViz html-widget"></div>
<script type="application/json" data-for="htmlwidget-b726cd6f19709e90cb0f">{"x":{"diagram":"\ndigraph {\n  rankdir = LR;\n  bgcolor = transparent;\n  node[label = \"\"; style = \"filled\"; fillcolor = \"#8DA0CB\"];\n\n  t2;\n\n  b0 -> b1 -> b2 -> b3[style = invis];\n  m0 -> m1 -> m2 -> m3;\n  t0 -> t1 -> t2[style = invis];\n\n  m1 -> t2 -> m3[constraint = false];\n  m2 -> b3[constraint = false];\n\n  b0, b1, b2, t0, t1[style = invis];\n}","config":{"engine":"dot","options":null}},"evals":[],"jsHooks":[]}</script><!--/html_preserve-->

---
# Submodules

.pull-left[
```
# key
parent_repo/
├── child_repo_1  # submodule 1
└── child_repo_2  # submodule 2

# example 1
talk or publication/
├── research_project_1
└── research_project_2
```
]

.pull-right[
```
# example 2
meta-analysis/
├── research_project_1
├── ...
└── research_project_n

# example 3
big-project/
├── *web-app*  -> also installed on web server
├── *lab-exp*  -> also installed on lab computers
├── *r-pkg*    -> installed by anyone who wants the data
├── conference
└── journal
```
]

---
# Version control's dirty little secret

(It only really works on plaintext files.)

<div class="figure">
<img src="presentation_files/figure-html/excel-panic-1.png" alt="Excel panic. Well, did you make changes or didn't you??" width="672" />
<p class="caption">Excel panic. Well, did you make changes or didn't you??</p>
</div>

---
# The good news

Once you're working in plaintext, you can do lots of cool things.

- Full power of VCS (merge, blame, etc).
- Use free and open source tools (Unix).
- **Write dynamic documents.**

---
# Dynamic documents

- Philosophy: DRY, Literate Programming
- Tools: Sphinx, Jupyter, Knitr, Pandoc

---
# Philosophy

.pull-left[
## Don't Repeat Yourself (DRY)

> Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.

Hunt & Thomas. (1999). _The pragmatic programmer_.
]

.pull-right[
## Literate programming (LP)

* Intermingle prose and code for better understanding of the program.
* The explanation of a program does not need to resemble the program structure.

Knuth, Donald E. (1983). _Literate programming_.
]

---
# Sphinx

**Python documentation generation**

* Python standard library: [json](https://docs.python.org/3/library/json.html)
* Third party packages: [requests](http://docs.python-requests.org/en/master/api/#requests.request)

---
# Project Jupyter

**Web-based, language-agnostic lab notebook.**

<img src="presentation_files/figure-html/jupyter-preview-1.png" width="672" />

---
# Knitr

**Elegant, flexible and fast dynamic report generation with R.**

    Participants in condition A outperformed participants in
    condition B, `report_model_results(mod, param = "condition")`.

<img src="presentation_files/figure-html/knitr-side-by-side-1.png" width="672" />

---
# Dynamic documents in practice

- Handouts
- Homework
- Supplemental materials
- Conference proceedings
- Journal papers

---
# A litmus test for reproducible research

Can you build the published paper without the original data?

### Building from source

- Open source tools
- No undocumented steps
- Centralized control

---
# Identical environments

.pull-left[
## Open source tools

- python
- R (S)
- Octave (Matlab)

## Virtual environments

- Enthought
- Anaconda
]

.pull-right[
## Cloud computing

- Amazon Web Services
- Open Stack

## Infrastructure-as-code

- ansible
- terraform
]

---
# Examples of "Building from source"

1. Kaggle leaderboards
2. Totems game

---
# Does it work?

<small>McKiernan, _et al._ (2016). How open science helps researchers succeed. _eLife_.</small>

<img src="presentation_files/figure-html/open-access-citations-1.png" width="672" />

---
# Cultural ratchets

.pull-left[
## Many species have elements of culture

- chimps (Whiten et al., 1999)
- whales (Garland et al., 2011)
- crows (Hunt & Gray, 2003)
]

.pull-right[
## Only humans exhibit **cumulative** culture

- ratchet effect (Tomasello et al., 1993)
- evolutionary process (Basalla, 1988)
- transmission fidelity (Lewis & Laland, 2012)
]

---
# Adoption open source practices for better science

Pierce Edmiston (<pedmiston@wisc.edu>)  
[github.com/pedmiston/reproducible-research](https://github.com/pedmiston/reproducible-research)  
[bit.ly/reproducible-research-refs](http://bit.ly/reproducible-research-refs)

Open source practices that make for more reproducible science:

1. Version control
2. Dynamic documents
3. Building from source

Conclusion: It's worth it!
