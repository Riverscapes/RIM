---
title: Riverscapes Report Card Template
weight: 1
---


<img class="float-right" src="https://riverscapes.net/assets/images/tools/grade/TRL_3_128w.png" alt="Research Grade">
<img class="float-left" width="150" alt="Tool Logo" src="{{ site.baseurl }}/assets/images/RIM_03.png"> **RIM** is an ArcGIS Toolbox and some ArcPy scripts that take care of file house keeping and metric calculation for mapping (i.e. digitizing) riverscape inundation paterns for individual "data capture events".  This report card communicates RIM's compliance with the Riverscape Consortium's published [tool standards](https://riverscapes.net/Tools).

# Report Card Summary

| Tool | [Riverscape Inundation Mapper (RIM) Tool](https://rim.riverscapes.net) |
| Version | [0.1.00](https://github.com/Riverscapes/RIM/releases/tag/v0.1.0) |
| Date of Review | 2022, October |
| Assessment Team | Names and/or Links |
| Current Assessment | ![research](https://raw.githubusercontent.com/Riverscapes/riverscapes-website/master/assets/images/tools/grade/TRL_3_32p.png) [Research Grade](https://riverscapes.net/Tools/discrimination.html#tool-grade) |
| Target Status | ![research](https://raw.githubusercontent.com/Riverscapes/riverscapes-website/master/assets/images/tools/grade/TRL_3_32p.png) [Research Grade](https://riverscapes.net/Tools/discrimination.html#tool-grade) → No further development as its own tool, Getting subsumed into  ![professional](https://raw.githubusercontent.com/Riverscapes/riverscapes-website/master/assets/images/tools/grade/TRL_5_32p.png) [Professional Grade](https://riverscapes.net/Tools/discrimination.html#professional-grade) [QRiS](https://qris.riverscapes.net)|
| Riverscapes Compliance | ![Riverscapes Compliant](https://riverscapes.net/assets/images/rc/RiverscapesCompliantPending_28.png) [Pending Riverscapes Compliance](https://riverscapes.net/Tools/#riverscapes-compliant-tools) - Because it is Research Grade |
| Assessment Rationale | 1-3 Sentence Summary by reviewers justifying assessment determination and summarizing from details below. |



# Report Card Details

This tool's [discrimination](https://riverscapes.net/Tools/discrimination#model-discrimination) evaluation by the [Riverscapes Consortium's](https://riverscapes.net) is:

**Evaluation Key:**
None or Not Applicable: <i class="fa fa-battery-empty" aria-hidden="true"></i> •
Minimal or In Progress: <i class="fa fa-battery-quarter" aria-hidden="true"></i> •
Functional: <i class="fa fa-battery-half" aria-hidden="true"></i> •
Fully Developed: <i class="fa fa-battery-full" aria-hidden="true"></i>  

| Criteria | Value | Evaluation | Comments and/or Recommendations |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| :----------------------------- | :----------------------------- |  | :----------------------------- |
| [Tool Interface(s)]({{ site.baseurl }}/Tools/discrimination.html#interface) | <i class="fa fa-terminal" aria-hidden="true"></i>  ArcPy Python Scripts   | <i class="fa fa-battery-half" aria-hidden="true"></i> | While the ArcPy scripts are functional, they are also fragile (typical of many toolboxes and code with ArcPy dependencies). |
| Scale | Reach (cell scale resolution, reach scale extent) | <i class="fa fa-battery-full" aria-hidden="true"></i> | This toolbox really creates empty feature classes with consistent attributes and naming, to allow the user to digitize riverscape inundation paterns and features at the reach-scale. The user chooses the basemaps (and therefore resolution of imagery), and can decide how detailed to digitize the features. |
| Language(s) and Dependencies | dependencies | <i class="fa fa-battery-half" aria-hidden="true"></i> | Comments. |
| Vetted in Peer-Reviewed Literature | Pending review in ESPL. Vetted as Masters Thesis: Bartelt [2021](https://doi.org/10.26076/a66b-0708) | <i class="fa fa-battery-three-quarters" aria-hidden="true"></i> | Awaiting peer review of manuscript. Thesis: - Bartelt K. 2021. Valley Bottom Inundation Patterns in Beaver-Modified Streams: A Potential Proxy for Hydrologic Inefficiency, Masters Thesis, Utah State University: Logan, UT. Available from: [https://digitalcommons.usu.edu/etd/8226](https://digitalcommons.usu.edu/etd/8226). DOI: [10.26076/a66b-0708](https://doi.org/10.26076/a66b-0708). |
| Source Code Documentation | Some comments in source code, and some troubleshooting clear from commit history. | <i class="fa fa-battery-quarter" aria-hidden="true"></i> | Missing ReadMe file. Also, no documentation on specific Python and ArcPy dependencies. |
| Open Source | [Open Source](https://github.com/Riverscapes/RIM) <i class="fa fa-github" aria-hidden="true"></i> with [GNU General Public License v 3.0](https://github.com/Riverscapes/gcd/blob/master/LICENSE) | <i class="fa fa-battery-full" aria-hidden="true"></i> | Follows Riverscape Compliance standards.  |
| Tool and Source Code Citable | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7265508.svg)](https://doi.org/10.5281/zenodo.7265508) | <i class="fa fa-battery-full" aria-hidden="true"></i> | Karen Barelt, Joe Wheaton, Matt Reimer, Margaret Hallerud, Philip Bailey, & Jordan Gilbert. (2022). Riverscapes Inundation Mapper - RIM 0.1 (v0.1.0). Zenodo. [https://doi.org/10.5281/zenodo.7265508](https://doi.org/10.5281/zenodo.7265508]) |
| User Documentation | Basic documentation on [Running the RIM Tool]({{ sitebase.url }}/Documentation/running/) and a [Protocol]({{ site.baseurl}}/Documentation/Protocols/). For users looking to visualize [outputs]({{ site.baseurl }}/Examples/ExampleData), there are a [few videos]({{ site.baseurl }}/Documentation/Viewing.html)). | <i class="fa fa-battery-quarter" aria-hidden="true"></i> | There is basic, minimal documentation that complies with the [Tool Website Documentation Standards](https://riverscapes.net/Tools/Technical_Reference/Documentation_Standards/WebSites/). However, the help could be elaborated and improved with some video tutorials.  |
| Easy User Interface | Basic ArcPy Toolboxes with limited help.                                                       | <i class="fa fa-battery-quarter" aria-hidden="true"></i> | These are really basic research scripts and toolboxes. Those familiar with using and loading Toolboxes in ArcGIS 10.X will find the [workflows]({{ sitebase.url }}/Documentation/running/) familiar.    |
| Scalability | Desc. | <i class="fa fa-battery-half" aria-hidden="true"></i> | Comments. |
|  Produces [Riverscapes Projects]({{ site.baseurl }}/Tools/Technical_Reference/Documentation_Standards/Riverscapes_Projects/) <img  src="https://riverscapes.net/assets/images/data/RiverscapesProject_24.png"> | Tool is outputting to disk data in a Riverscapes Project that can be opened in [RV](http://rave.riverscapes.net). | <i class="fa fa-battery-three-quarters" aria-hidden="true"></i> | Comments.  |

## F-A-I-R Assessment

 **F**-**A**-**I**-**R**, corresponds to the **f**indable, **a**ccessible, **i**nteroperable and **r**e-useable [Principles](https://force11.org/info/the-fair-data-principles/) (Wilkinson et al. [2016](https://www.nature.com/articles/sdata201618)), which the RC strives to follow and to help facilitate making it easier for the riverscapes community to follow. **F**-**A**-**I**-**R** can apply to metadata, data and the tool itself.




| FAIR Principle    | Value | Evaluation                                             | Comments  |
| ----------------- | ----- | ------------------------------------------------------ | --------- |
| **METADATA**      |       |                                                        |           |
| **F**indable      | Desc. | <i class="fa fa-battery-empty" aria-hidden="true"></i> | Comments. |
| **A**vailable     | Desc. | <i class="fa fa-battery-empty" aria-hidden="true"></i> | Comments. |
| **I**nteroperable | Desc. | <i class="fa fa-battery-empty" aria-hidden="true"></i> | Comments. |
| **R**e-useable    | Desc. | <i class="fa fa-battery-empty" aria-hidden="true"></i> | Comments. |
| **DATA**          |       |                                                        |           |
| **F**indable      | Desc. | <i class="fa fa-battery-empty" aria-hidden="true"></i> | Comments. |
| **A**vailable     | Desc. | <i class="fa fa-battery-empty" aria-hidden="true"></i> | Comments. |
| **I**nteroperable | Desc. | <i class="fa fa-battery-empty" aria-hidden="true"></i> | Comments. |
| **R**e-useable    | Desc. | <i class="fa fa-battery-empty" aria-hidden="true"></i> | Comments. |
| **TOOL**          |       |                                                        |           |
| **F**indable      | Desc. | <i class="fa fa-battery-empty" aria-hidden="true"></i> | Comments. |
| **A**vailable     | Desc. | <i class="fa fa-battery-empty" aria-hidden="true"></i> | Comments. |
| **I**nteroperable | Desc. | <i class="fa fa-battery-empty" aria-hidden="true"></i> | Comments. |
| **R**e-useable    | Desc. | <i class="fa fa-battery-empty" aria-hidden="true"></i> | Comments. |

Overall summary of tool **FAIR**-ness <i class="fa fa-battery-quarter" aria-hidden="true"></i> : Tool evaluation summary.

## Tool Output Utility

All Riverscapes tools package up data in Riverscapes Projects. This section evaluates the utility of those outputs to end-users that are not running the tool, but instead leveraging its outputs.

| Criteria | Value | Evaluation | Comments |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|----------------------------------------------------------|--------------------------------|
| :----------------------------- | :----------------------------- | :----------------------------- | :----------------------------- |
| [RV](https://rave.riverscapes.net)- Compliant Riverscapes Projects <img  src="https://riverscapes.net/assets/images/data/RiverscapesProject_24.png">? | Desc. | <i class="fa fa-battery-empty" aria-hidden="true"></i> | Comments. |
| [RV](https://rave.riverscapes.net) Business Logic Defined? | Desc. | <i class="fa fa-battery-empty" aria-hidden="true"></i> | Comments. |
| Riverscapes Projects hosted in public-facing [Riverscapes Warehouse(s)](https://riverscapes.net/Data_Warehouses/#warehouse-explorer-concept) <img src="https://riverscapes.net/assets/images/data/RiverscapesWarehouseCloud_24.png"> | Desc. | <i class="fa fa-battery-empty" aria-hidden="true"></i> | Comments. |
| Riverscapes Projects connected to [Web-Maps](https://riverscapes.net/Data_Warehouses#web-maps) <i class="fa fa-map-o" aria-hidden="true"></i> | Desc. | <i class="fa fa-battery-empty" aria-hidden="true"></i> | Comments. |
| Riverscapes Projects connected to Field [Apps](https://riverscapes.net//Data_Warehouses#apps---pwas) <img src="https://riverscapes.net/assets/images/tools/PWA.png"> | Desc. | <i class="fa fa-battery-empty" aria-hidden="true"></i> | Comments. |

## Developer Intent

*Development team (not evaluation team) should provide 1-3 paragraphs and/or some bullets and/or figures describing where they hope to go in future releases.*

If you share the above vision, get in touch with the developers to support/fund the effort. 

--------------------
<a href="https://riverscapes.net"><img class="float-left" src="https://riverscapes.net/assets/images/rc/RiverscapesConsortium_Logo_Black_BHS_200w.png"></a>
The [Riverscapes Consortium's](https://riverscapes.net) Technical Committee provides report cards for tools either deemed as "[riverscapes-compliant](https://riverscapes.net/Tools/#riverscapes-compliant)" <img  src="https://riverscapes.net/assets/images/rc/RiverscapesCompliant_32.png"> or "[pending riverscapes-compliance](https://riverscapes.net/Tools/#tools-pending-riverscapes-compliance)" <img  src="https://riverscapes.net/assets/images/rc/RiverscapesCompliantPending_28.png">. 
