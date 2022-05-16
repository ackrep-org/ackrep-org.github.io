Title: Index
Date: 2017-11-05 18:49:00
Author: PLQ Dresden
save_as: index.html


# Overview

Traditionally, human knowledge is represented mainly in form of written natural language, symbolic formulas and pictures. The project **ACKREP** aims to supplement these representation forms with additional formal (i.e. machine interpretable) representations. The scope of this project is *control theory* and *control engineering* (subsumed under "automatic control").

This discipline is characterized by a wide range of application fields from different physical domains and by a heterogeneous methodical landscape from different areas of mathematics, engineering and computer science.

Basically, the motivation for ACKREP is to **facilitate knowledge transfer** both

- within the discipline of automatic control (i.e. within subdisciplines), as well as
- with areas of potential application (e.g. mechanical engineering, chemical process engineering, etc.).

How best to achieve these goals is an open question and subject to ongoing research. More specifically, *ACKREP Code* constitutes a repository of control-related problems and solutions (represented as executable code). The *Methodnet* is a more abstract formal representation of control-theoretic methods which can be applied to a concrete setting by linking them via a path-finding algorithm.

This research is carried out at the [Institute of Control Theory, TU Dresden](http://www.et.tu-dresden.de/rst/).


# Subprojects

**Important notice:** Our current attempts of formal knowledge representation are still very experimental. We highly encourage anybody interested in this topic to contact the [ackrep-team](#team) with questions, feedback and/or contribution ideas.

## *ACKREP Code*

Large parts of control knowledge are comprised of algorithms and are available as executable code, e.g. feedback design, trajectory planning, observability checking etc. However, often this code is not published or at least hard to execute on different environments. This clearly hinders **reproducibility** and thus knowledge transfer. In [1.1] we therefore propose *ACKREP Code* (originally just named "ACKRep"): A Git repository which holds control-related code in a special structure (*problems*, *solutions*, *methods*, *environment specifications*, ...) plus a webservice which checks the solution-entities against the problem-entities, i.e. a specialized continuous integration service.

References:

- [1.1] Carsten Knoll und Robert Heedt: *„‚Automatic Control Knowledge Repository‘ – A Computational Approach for Simpler and More Robust Reproducibility of Results in Control Theory“*. In:
24th International Conference on System Theory, Control and Computing (ICSTCC). 2020, P. 130–136. [Fulltext of Preprint](downloads/2020_Knoll_Heedt__ICSTCC__Automatic_Control_Knowledge_Repository__preprint.pdf)
- [1.2] Conference Presentation: [One-Page-Summary](img/2020_Knoll_Heedt__ICSTCC__Automatic_Control_Knowledge_Repository__summary.png) | [PDF-Slides](downloads/2020_Knoll_Heedt__ICSTCC__Automatic_Control_Knowledge_Repository__slides.pdf) | [Video](downloads/2020_Knoll_Heedt__ICSTCC__Automatic_Control_Knowledge_Repository__talk-video.mp4)
- [1.3] Carsten Knoll und Robert Heedt: *Tool-based Support for the FAIR Principles for Control Theoretic Results: The “Automatic Control Knowledge Repository”* [Fulltext of Preprint](downloads/2021_Knoll_Heedt__STCCJ__FAIR_Principles_Automatic_Control_Knowledge_Repository__preprint.pdf)

- [1.4] Demo instance: <https://testing.ackrep.org>



## *Methodnet*

In [2.1] we propose the *Methodnet*, a supplement to classical knowledge representation, consisting of types and methods in a graph structure.
From that, a schematic solution procedure can be generated for a specific problem.
"Trajectory tracking control for a triple pendulum" is used to demonstrate how the proposed method supports knowledge transfer.
Furthermore, an OWL-**ontology** is automatically generated from the methodnet which allows accessing this knowledge base with **SPARQL** and other semantic methods.

Note: Currently, information about this project is only available in German.

References:

- [2.1] Robert Heedt, Carsten Knoll, Klaus Röbenack: *„Formal Semantic Representation of Methods in Automatic Control“*, Submitted to VDI Mechatronik-Tagung, 2021, (German). [Fulltext of Preprint](downloads/2021_Heedt_Knoll_Roebenack__VDI_Mechatronik__Formale_semantische_Repraesentation_regelungstechnischer_Methoden__preprint.pdf)
- [2.2] Demo instance: <https://methodnet.ackrep.org>


# Team

- [Carsten Knoll](https://tu-dresden.de/ing/elektrotechnik/rst/das-institut/beschaeftigte/carsten-knoll)
- [Julius Fiedler](https://tu-dresden.de/ing/elektrotechnik/rst/das-institut/beschaeftigte/)
- [Anne Harloff](https://tu-dresden.de/ing/elektrotechnik/rst/das-institut/beschaeftigte/)
- [Robert Heedt](https://tu-dresden.de/ing/elektrotechnik/rst/das-institut/beschaeftigte/robert-heedt)
