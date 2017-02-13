---
title: Adopting open source practices for better science
author: |
  Pierce Edmiston  
  <pedmiston@wisc.edu>  
  [sapir.psych.wisc.edu](http://sapir.psych.wisc.edu)  
  [github.com/pedmiston](https://github.com/pedmiston)
output:
  xaringan::moon_reader
---

# Outline

Open source practices that make for more reproducible science:

1. Version control
2. Dynamic documents
3. Building from source

Conclusion: It's worth it!



---
# Why I care about reproducibility

<small>Open Science Collaboration. 2015. Estimating the reproducibility of psychological science. _Science_. [url](http://science.sciencemag.org/content/349/6251/aac4716).</small>

<img src="presentation_files/figure-html/unnamed-chunk-2-1.png" width="672" />

???

There are two reasons I care about reproducibility. The first is that I worry about the reproducibility of my own research. I only know about my field of psychology, but at least in psychology it's pretty easy to conduct a study, explore the data, and come to a conclusion that can't be repeated. Here's a plot from a paper reporting the results of a massive replication effort where they replicated 100 published studies and found that less than 40% of the original effects were replicated. Reproducibility is fundamental to scientific progress, but just because something is published, it doesn't mean it will necessarily replicate. Here's how they put it in the paper:

> Scientific claims should not gain credence because of the status or authority of their originator but by the replicability of their supporting evidence.

---
# Why isn't psychological research more reproducible?

- Simmons, Nelson, & Simonsohn. (2011). False-positive psychology: undisclosed flexibility in data collection and analysis allows presenting anything as significant. _Psychological Science_. [url](http://doi.org/10.1177/0956797611417632).
- Gelman & Loken (2013). The garden of forking paths: Why multiple comparisons can be a problem, even when there is no “fishing expedition” or “p-hacking” and the research hypothesis was posited ahead of time. Unpublished manuscript. [url](http://www.stat.columbia.edu/~gelman/research/unpublished/p_hacking.pdf).
- Palmeri, K. 2016. Psychology is in crisis over whether it's in crisis. _WIRED_. [url](https://www.wired.com/2016/03/psychology-crisis-whether-crisis/).
- Ioannidis, J. 2005. Why most published research findings are false. _PLOS Medicine_. [url](http://dx.doi.org/10.1371/journal.pmed.0020124).

???

It's interesting that the title of the paper is "Estimating the reproducibility of psychological science" because it doesn't necessarily mean we expect 100% of our research findings to replicate or indeed that a single failure to replicate indicates that a paper needs to be retracted. It's a genuine question: What is the reproducibility of psychological science? Can we measure it? And the most importantly, can we improve it? Nonetheless 40% is pretty low, and we should consider why the reproducibility of psychological science might be lower we might expect.

Perhaps not surprisingly, people disagree as to what the cause of the reproducibility crisis is. This paper from 2011 called "False-positive psychology" documents many of the ways in which common research practices might result in results that can't be reproduced. In the paper they have people complete a survey with very random and unmotivated survey questions, and through some strategic exclusions find "significant" results. In this case they were searching for statistically significant findings, or "p-hacking", and doing so consciously, but even less malicious analysis practices may lead to results that don't replicate. Andrew Gelman in an unpublished paper calls this the "garden of forking paths" in reference to a Jorge Luis Borges short story where a man encounters various versions of himself in slightly different universes. Gelman and Loken's argument is that because we conduct our statistical analysis in a sequential way, pursuing particular results until we find them and then stopping, null hypothesis testing is the real enemy of the reproducibility crisis.

Of course, many people have pointed out that these issues are not new, and that simulations of research findings don't necessarily reflect actual research that is done and published, and that failures to replicate on their own simply don't tell us much. It was to the point that there was a WIRED article written about the controversy over whether psychology was indeed in crisis or not.

However, I don't think any of this is specific to psychology, and indeed the argument has been made by John Ioannidis and others that it's really a broader problem with the way scientific research is conducted and specifically how it's published. A publication by itself cannot be used as an indisputable unit of scientific fact. We need to stop thinking about experiments as one-off events and try to build in a meta-analytic perspective that seeks to unify datasets.

---
# Why open source is the answer

A researcher says  
> My collaborators should be able to reproduce my research.  

An open source community member says  
> Anyone should be able to use and contribute to this project.

???

To illustrate why I think open source is the answer to problems with reproducibility, consider the following goals of reproducibility in science and in the open source community.

Reproducibility in a research setting is often framed in terms of collaboration on a particular research project. A researcher might say that her goal is that her collaborators can reproduce her research. All researchers expect their research to be reproducible at least by the people working within the same lab or on the same project. This is generally considered a pretty low bar, and yet it's not always achieved.

Compare that to the goal of the open source community member, who wants anyone--absolutely anyone--to be able to use and contribute to their open source project. Doesn't matter where they live or work or in many cases what they do with the source code, but their goal is that everyone should be able to share a computer program and contribute to it's writing.

I think looking to open source is the answer because they've done much better at reproducibility than I have. They've solved many of the most difficult problems for us, and now all we have to do is use them in our own research to make it more reproducible.

---
# Open source science

> Rather than thinking about reproducibility as redundancy and confidence, shift to thinking about reproducibility as collaboration and progress.

---
# Version control

<div class="figure">
<img src="presentation_files/figure-html/unnamed-chunk-3-1.png" alt="Version control in the wild." width="1152" />
<p class="caption">Version control in the wild.</p>
</div>

---
# Tools for climbing

<img src="presentation_files/figure-html/unnamed-chunk-4-1.png" width="672" />

---
# Pick your poison

- **git**
- mercurial
- subversion

???

My requirements for choosing version control system are that it is **open source** and supports **distributed** collaboration and merge operations, which most modern VCSs do.

---
# Forks and branches

<!--html_preserve--><div id="htmlwidget-17ae09b18809ce1affe5" style="width:672px;height:200px;" class="grViz html-widget"></div>
<script type="application/json" data-for="htmlwidget-17ae09b18809ce1affe5">{"x":{"diagram":"\ndigraph {\n  rankdir = LR;\n  node[label = \"\"];\n  m0 -> m1 -> m2 -> m3;\n  b0, b1[style = invis];\n  b0 -> b1 -> b2[style = invis];\n  b2 -> b3;\n  m1 -> b2[constraint = false];\n}","config":{"engine":"dot","options":null}},"evals":[],"jsHooks":[]}</script><!--/html_preserve-->

---
# Submodules

    talk or publication/
    ├── research_project_1
    └── research_project_2

    meta-analysis/
    ├── research_project_1
    ├── ...
    └── research_project_n

    project/
    ├── *web-app*  -> also installed on web server
    ├── *psychopy* -> also installed on lab computers
    ├── *r-pkg*    -> installed by anyone who wants the data
    ├── conference
    └── journal

---
# Dynamic documents

---
# Origins of dynamic documents

## Don't Repeat Yourself (DRY)

> Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.

- Hunt & Thomas, 1999, _The pragmatic programmer_. [wiki](https://en.wikipedia.org/wiki/The_Pragmatic_Programmer).

## Literate programming (LP)

Knuth, Donald E. (1983). _Literate programming_. [wiki](https://en.wikipedia.org/wiki/Literate_programming).

* Intermingle prose and code for better understanding of the program.
* The explanation of a program does not need to resemble the program structure.

---
# Sphinx

## Python Documentation Generation

* Python standard library: [json](https://docs.python.org/3/library/json.html)
* Third party package: [requests](http://docs.python-requests.org/en/master/api/#requests.request)

---
# Project Jupyter

<img src="presentation_files/figure-html/unnamed-chunk-6-1.png" width="672" />

---
# Knitr

## Elegant, flexible and fast dynamic report generation with R

Participants in condition A outperformed participants in condition B, `report_model_results(mod, param = "condition")`.

---
# Knitr (continued):

No more copying static image files!

    `\`\`\``  
    `{r eval=FALSE}`  
    `plot(df)`  
    `\`\`\``

---
# Dynamic documents in science

- Supplemental materials
- Entire manuscripts

> Using dynamic documentation enforces reproducibility, facilitates replication efforts, and encourages the extension of research projects beyond publication.

---
# Building from source
