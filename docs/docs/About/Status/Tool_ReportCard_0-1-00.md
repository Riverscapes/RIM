---
title: Riverscapes Report Card - RIM 0.1.0
sidebar_position: 1
---


![Research Grade](https://riverscapes.net/assets/images/tools/grade/TRL_3_128w.png)

![Tool Logo](/img/RIM_03.png)

**RIM** consists of some ArcPy scripts that take care of file housekeeping and metric calculation for mapping (i.e. digitizing) riverscape inundation patterns for individual "data capture events".  This report card communicates RIM's compliance with the Riverscape Consortium's published [tool standards](https://riverscapes.net/Tools).

# Report Card Summary

| **Field** | **Value** |
|---|---|
| Tool | [Riverscape Inundation Mapper (RIM) Tool](https://rim.riverscapes.net) |
| Version | [0.1.00](https://github.com/Riverscapes/RIM/releases/tag/v0.1.0) |
| Date of Review | 2022, October |
| Assessment Team | Wheaton & Gilbert |
| Current Assessment | ![research](https://raw.githubusercontent.com/Riverscapes/riverscapes-website/master/assets/images/tools/grade/TRL_3_32p.png) [Research Grade](https://riverscapes.net/Tools/discrimination.html#tool-grade) |
| Target Status | ![research](https://raw.githubusercontent.com/Riverscapes/riverscapes-website/master/assets/images/tools/grade/TRL_3_32p.png) [Research Grade](https://riverscapes.net/Tools/discrimination.html#tool-grade) → No further development as its own tool, Getting subsumed into ![professional](https://raw.githubusercontent.com/Riverscapes/riverscapes-website/master/assets/images/tools/grade/TRL_5_32p.png) [Professional Grade](https://riverscapes.net/Tools/discrimination.html#professional-grade) [QRiS](https://qris.riverscapes.net) |
| Riverscapes Compliance | ![Riverscapes Compliant](https://riverscapes.net/assets/images/rc/RiverscapesCompliantPending_28.png) [Pending Riverscapes Compliance](https://riverscapes.net/Tools/#riverscapes-compliant-tools) - Because it is Research Grade |
| Assessment Rationale | The RIM Tool 0.1.0 is very deserving of both a [Research Grade](https://riverscapes.net/Tools/discrimination.html#tool-grade) distinction and [Pending Riverscapes Compliance](https://riverscapes.net/Tools/#riverscapes-compliant-tools). It is a perfect example of where we hope researchers and graduate students can get a tool (without too much extra work), so that at least the outputs of the tool can be [**F**-**A**-**I**-**R**](https://rim.riverscapes.net/About/Status/Tool_ReportCard_0-1-00.html#f-a-i-r-assessment) even if the tool itself is only likely to be reused by a small number. Refactoring this tool into its own Professional Grade tool (or as planned, as part of [QRiS](https://qris.riverscapes.net)) is straight forward, but also beyond the scope of a Masters or most PhDs (requires professional software development help). Though the tool is not *ready* to be used by large audiences, the protocol it lays out is, and the [riverscape project datasets](https://rim.riverscapes.net/Examples/ExampleData.html) it packages are highly consumable. |



# Report Card Details

This tool's [discrimination](https://riverscapes.net/Tools/discrimination#model-discrimination) evaluation by the [Riverscapes Consortium's](https://riverscapes.net) is:


**Evaluation Key:**
None or Not Applicable: <i class="fa fa-battery-empty" aria-hidden="true"></i> •
Minimal or In Progress: <i class="fa fa-battery-quarter" aria-hidden="true"></i> •
Functional: <i class="fa fa-battery-half" aria-hidden="true"></i> •
Fully Developed: <i class="fa fa-battery-full" aria-hidden="true"></i>

| **Criteria** | **Value** | **Evaluation** | **Comments and/or Recommendations** |
|---|---|---|---|
| [Tool Interface(s)](https://riverscapes.net/Tools/discrimination.html#interface) | ArcPy Python Scripts | <i class="fa fa-battery-half" aria-hidden="true"></i> | While the ArcPy scripts are functional, they are also fragile (typical of code with ArcPy dependencies). |
| Scale | Reach (cell scale resolution, reach scale extent) | <i class="fa fa-battery-full" aria-hidden="true"></i> | This toolbox really creates empty feature classes with consistent attributes and naming, to allow the user to digitize riverscape inundation patterns and features at the reach-scale. The user chooses the basemaps (and therefore resolution of imagery), and can decide how detailed to digitize the features. |
| Language(s) and Dependencies | dependencies | <i class="fa fa-battery-half" aria-hidden="true"></i> | The python scripts have ArcPy dependencies (ESRI). |
| Vetted in Peer-Reviewed Literature | Pending review in ESPL. Vetted as Masters Thesis: Bartelt [2021](https://doi.org/10.26076/a66b-0708) | <i class="fa fa-battery-three-quarters" aria-hidden="true"></i> | Awaiting peer review of manuscript. Thesis: - Bartelt K. 2021. Valley Bottom Inundation Patterns in Beaver-Modified Streams: A Potential Proxy for Hydrologic Inefficiency, Masters Thesis, Utah State University: Logan, UT. Available from: [https://digitalcommons.usu.edu/etd/8226](https://digitalcommons.usu.edu/etd/8226). DOI: [10.26076/a66b-0708](https://doi.org/10.26076/a66b-0708). |
| Source Code Documentation | Some comments in source code, and some troubleshooting clear from commit history. | <i class="fa fa-battery-quarter" aria-hidden="true"></i> | Missing ReadMe file. Also, no documentation on specific Python and ArcPy dependencies. |
| Open Source | [Open Source](https://github.com/Riverscapes/RIM) with [GNU General Public License v 3.0](https://github.com/Riverscapes/gcd/blob/master/LICENSE) | <i class="fa fa-battery-full" aria-hidden="true"></i> | Follows Riverscape Compliance standards (see [issue #1](https://github.com/Riverscapes/RIM/issues/1)). |
| Tool and Source Code Citable | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7265508.svg)](https://doi.org/10.5281/zenodo.7265508) | <i class="fa fa-battery-full" aria-hidden="true"></i> | Karen Barelt, Joe Wheaton, Matt Reimer, Margaret Hallerud, Philip Bailey, & Jordan Gilbert. (2022). Riverscapes Inundation Mapper - RIM 0.1 (v0.1.0). Zenodo. [https://doi.org/10.5281/zenodo.7265508](https://doi.org/10.5281/zenodo.7265508]) |
| User Documentation | Basic documentation on [Running the RIM Tool](/docs/Documentation/running/) and a [Protocol](/docs/Documentation/Protocols/). For users looking to visualize [outputs](/docs/Examples/ExampleData), there are a [few videos](/docs/Documentation/Viewing.html). | <i class="fa fa-battery-quarter" aria-hidden="true"></i> | There is basic, minimal documentation that complies with the [Tool Website Documentation Standards](https://riverscapes.net/Tools/Technical_Reference/Documentation_Standards/WebSites/). However, the help could be elaborated and improved with some video tutorials. |
| Easy User Interface | Basic ArcPy scripts with no help. | <i class="fa fa-battery-quarter" aria-hidden="true"></i> | These are really basic research scripts. Those familiar with ArcPy from command prompt in ArcGIS 10.X will find the workflows familiar. |
| Scalability | The scripts have ArcPy depencencies and since ArcGIS 10.x is a 32-Bit software, memory problems are possible (i.e. 4GB RAM). However, since the tool is primarily intended to be used on reach-scale, hand digitized riverscape data, these issues are probably not realized. | <i class="fa fa-battery-quarter" aria-hidden="true"></i> | There is nothing complicated in this that couldn't easily be reafactored to opensource GIS and written to handle larger datasets. The project sizes are bloated primarily because of the UAV rasters (typically 2.5 to 7 cm resolution and often > 1 GB each). There is also a lot of storage in the contextual layers (e.g. DEM), which span an entire watershed. Watershed Attribute Tool and other projects in QRiS could keep the actual data here (i.e. digitized layers) much more compact and separate out the bases into their own projects. |
| Produces [Riverscapes Projects](https://riverscapes.net/Tools/Technical_Reference/Documentation_Standards/Riverscapes_Projects/) <i class="fa fa-database" aria-hidden="true"></i> | Tool is outputting to disk data in a Riverscapes Project that can be opened in [RV](http://rave.riverscapes.net). | <i class="fa fa-battery-three-quarters" aria-hidden="true"></i> | The business logic and symbology has been nicely curated and works well in QRV and ArcRV. However, the rasters still do not display nicely in WebRAVE (see [issue #14](https://github.com/Riverscapes/RIM/issues/14)). |

## F-A-I-R Assessment

 **F**-**A**-**I**-**R**, corresponds to the **f**indable, **a**ccessible, **i**nteroperable and **r**e-useable [Principles](https://force11.org/info/the-fair-data-principles/) (Wilkinson et al. [2016](https://www.nature.com/articles/sdata201618)), which the RC strives to follow and to help facilitate making it easier for the riverscapes community to follow. **F**-**A**-**I**-**R** can apply to metadata, data and the tool itself.




| FAIR Principle | Value | Evaluation | Comments |
| --- | --- | --- | --- |
| **METADATA**      |       |                                                        |           |
| **F**indable      | Yes with [RAVE](https://rave.riverscapes.net). | Battery Half | [Riverscapes Projects](https://riverscapes.net/Tools/Technical_Reference/Documentation_Standards/Riverscapes_Projects/) ![Riverscapes Project Icon](https://riverscapes.net/assets/images/data/RiverscapesProject_24.png) are used, Metadata is easy to incorporate. Good project level metadata is included and easy to find in RAVE and Warehouse. However, there is virtually no layer level metadata the tool writes. The notable exceptions are the Basemaps (thank you). Even the context layers that come from other Riverscapes Project don't bring the Metadata along. |
| **A**vailable     | Well, yes, the Metadata is available easily through Warehouse and RAVE. | Battery Quarter | Low score provided because not much is populated to be available. |
| **I**nteroperable | Yes, compliant with [Warehouse Standards](https://riverscapes.net/Data_Warehouses/) | Battery Full | This gets a full-score just for being Riverscapes-Compliant projects.|
| **R**e-useable    | Yes, but again needs full populating. | Battery Quarter | Easy to consume, but not enough to consume. Incomplete. |
| **DATA**          |       |                                                        |           |
| **F**indable      | Easily findable in Warehouse.| Battery Full | Current version of Warehouse requires account to access data. Also no DOIs currently minted. Easy to address in next version of Warehouse and with Zenodo. |
| **A**vailable     | Data that developer produced with tool is [available in warehouse](https://rim.riverscapes.net/Examples/ExampleData.html) | Battery Full | Will benefit from improvements in new releasees of warehouse without developer needing to do anything. |
| **I**nteroperable | Most of the data is geospatial and in standard shapefile and raster formats. Other data is simple CSV, images and PDFs. All are easy to work with in multiple GIS platforms. | Battery Half | Although these are standard data outputs, the feature classes could have improved interoperability in geopackages (i.e. as SQLite databases) and easier to harvest info, while ditching sidecar files of shapefiles. The rasters are nice geoTIFF formats and compressed. |
| **R**e-useable    | Primary outputs are GIS and because of [Riverscapes Projects](https://riverscapes.net/Tools/Technical_Reference/Documentation_Standards/Riverscapes_Projects/) ![Riverscapes Project Icon](https://riverscapes.net/assets/images/data/RiverscapesProject_24.png) pacaging, these are highly resuseable | Battery Full | Nice job. |
| **TOOL**          |       |                                                        |           |
| **F**indable      | Tool is clearly available as opensource in GitHub and tracked in Zendo (see [here](https://rim.riverscapes.net/About/license.html)) | Battery Full | Follows best standards of practice. |
| **A**vailable     | Same as above. | Battery Full | Follows best standards of practice |
| **I**nteroperable | Limited to version specific ArcPy and ArcGIS 10.X. | Battery Quarter | ArcPy is notoriously fragile between versions and very difficult to deploy these scripts on others machines. It is possible, but not easy. |
| **R**e-useable    | See comments above. | Battery Quarter | This is not a highly reusable tool by GIS users nor is it likely to be used extensively by other developers. However, it is transparently laid out to make it clear what was done and because [protocol](https://rim.riverscapes.net/Documentation/Protocols/) and methods are compelling, acts as excellent pseudocode for future developers in a refactor. |

Overall summary of tool **FAIR**-ness (Battery Quarter): The datasets packaged as riverscapes projects and hosted in the warehouse are the most compelling FAIR aspects of this tool. Everything (metadata, data, tool) is **F**indable and **A**vailable, but primarily the data output itself is **I**nteroperable and really **R**euseable.

## Tool Output Utility

All Riverscapes tools package up data in Riverscapes Projects. This section evaluates the utility of those outputs to end-users that are not running the tool, but instead leveraging its outputs.

| Criteria | Value | Evaluation | Comments |
| --- | --- | --- | --- |
| [RV](https://rave.riverscapes.net)-Compliant Riverscapes Projects<br/>![Riverscapes Project Icon](https://riverscapes.net/assets/images/data/RiverscapesProject_24.png) | Checkmark: Nicely and logically packaged projects. | Battery Three-Quarters | A few minor housekeeping things still identified (See issue [#14](https://github.com/Riverscapes/RIM/issues/14)). |
| [RV](https://rave.riverscapes.net) Business Logic Defined? | Checkmark: [Innundation.xml](https://github.com/Riverscapes/RiverscapesXML/blob/master/RaveBusinessLogic/V1/Inundation.xml) | Battery Three-Quarters | A few minor issues around polygons still incorrectly identified as polylines. Easy fixes. |
| Riverscapes Projects hosted in public-facing [Riverscapes Warehouse(s)](https://riverscapes.net/Data_Warehouses/#warehouse-explorer-concept)<br/>![Warehouse Cloud Icon](https://riverscapes.net/assets/images/data/RiverscapesWarehouseCloud_24.png) | Checkmark: See [Example Data](https://rim.riverscapes.net/Examples/ExampleData.html) | Battery Empty |  |
| Riverscapes Projects connected to [Web-Maps](https://riverscapes.net/Data_Warehouses#web-maps) | Checkmark: See [Exploring RIM Project in Web RV](https://rim.riverscapes.net/Documentation/Viewing.html#exploring-rim-project-in-web-rv). | Battery Half | Thanks to WebRV, yes there are nice webmaps. However, the raster resolution of the key bases (i.e. basemaps) are so ridiculously downgraded for tileizing that it really limits the ability of the user to evaluate without downloading to desktop GIS. This is a problem (see issue [#486](https://github.com/Riverscapes/RiverscapesXML/issues/486)) |
| Riverscapes Projects connected to Field [Apps](https://riverscapes.net/Data_Warehouses#apps---pwas)<br/>![PWA Icon](https://riverscapes.net/assets/images/tools/PWA.png) | No | Battery Empty | This is intended with [QRiS](https://qris.riverscapes.net) and QField. |

## Developer Intent

The [developers](https://rim.riverscapes.net/About/acknowledgements.html#rim-development-team) have no intent to take this version of RIM any further. It was intended from the start to help develop and vett the methods of mapping inundation paterns and get a protocol together. The tool was more of a proof-of-concept on the utility of the housekeeping and packaging and its value. Beyond the 39 sites in Bartelt ([2021](https://doi.org/10.26076/a66b-0708)), the [Utah State University Ecogeomorphology and Topographic Analysis Lab](http://etal.joewheaton.org) have worked with partners at [USFS PIBO](https://www.fs.usda.gov/detail/r4/landmanagement/resourcemanagement/?cid=stelprd3845865), USGS partners, and BLM partners and have applied the protocol on another 50+ sites across Western states.  In addition, [Anabranch Solutions](https://anabranchsolutions.com) has applied it for [LTPBR](https://lowtechpbr.restoration.usu.edu) planning and monitoring extensively in its projects.  
With pilot funding from NOAA, [USFS PIBO](https://www.fs.usda.gov/detail/r4/landmanagement/resourcemanagement/?cid=stelprd3845865), and [Anabranch Solutions](https://anabranchsolutions.com), the developers incorporated RIM into Beta releasaes of [QRiS](https://qris.riverscapes.net). An illustration is shown below:

[![RIM in QRIS](/img/RIM_in_QRIS.png)](/img/RIM_in_QRIS.png)


After the pilot work, [BLM](https://www.blm.gov/programs/aquatics) awarded USU a grant to take QRiS from a research-grade to a professional-grade tool with RIM fully incorporated. 

If you share the above vision, get in touch with the [developers](https://rim.riverscapes.net/About/acknowledgements.html#rim-development-team) to support/fund the effort. 

--------------------
<!-- ![Riverscapes Consortium Logo](https://riverscapes.net/assets/images/rc/RiverscapesConsortium_Logo_Black_BHS_200w.png) -->
The [Riverscapes Consortium's](https://riverscapes.net) Technical Committee provides report cards for tools either deemed as "[riverscapes-compliant](https://riverscapes.net/Tools/#riverscapes-compliant)"  or 
"
[pending riverscapes-compliance](https://riverscapes.net/Tools/#tools-pending-riverscapes-compliance)
" 
<!-- ![Pending Riverscapes Compliance Icon](https://riverscapes.net/assets/images/rc/RiverscapesCompliantPending_28.png). -->
