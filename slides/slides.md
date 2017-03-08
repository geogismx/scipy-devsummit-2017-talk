% Scientific Programming <br> with the SciPy Stack
% Shaun Walbridge; Kevin Butler

<section data-background="images/title.png">
<h2>[https://github.com/scw/scipy-devsummit-2017-talk](https://github.com/scw/scipy-devsummit-2017-talk)</h2>
<h3>[High Quality PDF (5MB)](https://4326.us/esri/scipy-2017/devsummit-2017-scipy-arcgis-presentation-full.pdf)</h3>
<h3>[Resources Section](https://4326.us/esri/scipy-2017/#resources)</h3>
</section>

Scientific Computing {data-background="images/Picture2.jpg"}
====================

Scientific Computing {data-background="images/Picture2.jpg"}
--------------------

<div style="float: left; width: 50%">
![](images/scientific-computing-wheel-diagram.png){class="tight"}
</div>
<div style="float: right; width: 45%; text-align: left; padding-top: 20px">
The application of computational methods to all aspects of the process of scientific investigation – data acquisition, data management, analysis, visualization, and sharing of methods and results.
</div>

Extending ArcGIS {data-background="images/Picture2.jpg"}
----------------

 - ArcGIS is a _system of record_. Combine data and analysis from many fields and into a common environemnt.
 - Why extend? Can't do it all, we support over 1000 GP tools &mdash; enabling _integration_ with other environments to extend the platform.


Python {data-background="images/Picture4.jpg"}
======

Why Python? {data-background="images/Picture4.jpg"}
-----------

 - Accessible for new-comers, and the [most taught first language in US universites](http://cacm.acm.org/blogs/blog-cacm/176450-python-is-now-the-most-popular-introductory-teaching-language-at-top-us-universities/fulltext)
 - Extensive package collection (56k on [PyPI](https://pypi.python.org/pypi)), broad user-base
 - Strong glue language used to bind together many environments, both open source and commercial
 - Open source with liberal license &mdash; do what you want

. . . 

<br>

* Brand new to Python? This talk may be challenging
* Resources include materials that for getting started

Python in ArcGIS {data-background="images/Picture4.jpg"}
----------------

 - Python API for driving ArcGIS Desktop and Server
 - A fully integrated module: ``import arcpy``
 - Interactive Window, Python Addins, Python Tooboxes
 - Extensions:
    + Spatial Analyst: ``arcpy.sa``
    + Map Document: ``arcpy.mapping``
    + Network Analyst: ``arcpy.na``
    + Geostatistics: ``arcpy.ga``
    + Fast cursors: ``arcpy.da``
 - ArcGIS API for Python

Python in ArcGIS {data-background="images/Picture4.jpg"}
----------------

 - Python 3.5 in Pro ([Desktop vs Pro Python](http://pro.arcgis.com/en/pro-app/arcpy/get-started/python-migration-for-arcgis-pro.htm))
    + ``arcpy.mp`` instead of ``arcpy.mapping``
 - Continue to add modules: NetCDF4, xlrd, xlwt, PyPDF2, dateutil, pip
 - [Python raster function](http://desktop.arcgis.com/en/desktop/latest/manage-data/raster-and-images/python-raster-function.htm), with a [repository of examples](https://github.com/Esri/raster-functions) using SciPy for on the fly visualizations

<div class="notes">
 - ``arcpy.mp`` Pro works with a conceptual model with _Project_ at the root, so this module reflects that difference from ArcMap where _map document_ is the root with ``arcpy.mapping``.
 - Modules galore: NetCDF4, xlrd, xlwt, PyPDF2, dateutil, pip, ...
</div>

Python in ArcGIS {data-background="images/Picture4.jpg"}
----------------

 * Here, focus on SciPy stack, what’s included out of the box
 * Move toward maintainable, reusable code and beyond the “one-off”
 * Recurring theme: multi-dimensional data structures
 * Also see [Brendan Collins talk tomorrow](https://devsummitps17.schedule.esri.com/session-catalog/216814585) which covers ``dask``

<div class="notes">
Multi-dimensional data structures -- numpy, pandas, our multi-d support all take advantage of different forms of an N-dimensional data structure. Rich, lets you pack simpler data into it for performance, still useful for 1D and 2D data!
</div>

SciPy  {data-background="images/Picture2.jpg"}
=====

Why SciPy? {data-background="images/Picture2.jpg"}
----------

* Most languages don’t support things useful for science, e.g.:
    + Vector primitives
    + Complex numbers
    + Statistics
* Object oriented programming isn’t always the right paradigm for 
   analysis applications, but is the only way to go in many modern languages
* SciPy brings the pieces that matter for scientific problems to Python.

SciPy Stack {data-background="images/Picture2.jpg"}
-----------

![](images/stack-circle.png){style="width: 600px"}

Included SciPy {data-background="images/Picture2.jpg"}
--------------

Package                                               KLOC     Contributors      Stars
-------                                             ------   --------------    -------
[matplotlib](http://matplotlib.org/)                   118              441     4909 
[Nose](http://readthedocs.org/docs/nose/en/latest/)      7               75     1053
[NumPy](http://www.numpy.org/)                         236              429     4011
[Pandas](http://pandas.pydata.org)                     183              408     8765
[SciPy](http://scipy.org/scipylib/)                    387              387     2930
[SymPy](http://sympy.org/)                             243              443     3642
Totals                                                1174             1885

Testing with Nose {data-background="images/Picture2.jpg"}
-----------------

 - [Nose](https://nose.readthedocs.org/en/latest/testing.html) &mdash; a Python framework for testing 
 - Tests improve your productivity, and create robust code
 - Nose builds on `unittest` framework, extends it to make testing easy.
 - Plugin architecture, [includes a number of plugins](https://nose.readthedocs.org/en/latest/plugins/builtin.html) and can be extended with [third-party plugins](https://nose-plugins.jottit.com/).


![](images/logos/numpy.png) {data-background="images/Picture2.jpg"}
---------------------------

  1. An array object of arbitrary homogeneous items
  2. Fast mathematical operations over arrays
  3. Random Number Generation

![](images/numpy-array.png)

[SciPy Lectures](https://scipy-lectures.github.io/intro/numpy/array_object.html#indexing-and-slicing), CC-BY

ArcGIS + NumPy {data-background="images/Picture2.jpg"}
--------------
 - ArcGIS and NumPy can interoperate on raster, table, and feature data.
 - See [Working with NumPy in ArcGIS](http://desktop.arcgis.com/en/desktop/latest/analyze/python/working-with-numpy-in-arcgis.htm)
 - In-memory data model. Example script to [process by blocks](../examples/process-by-blocks.py) if working with larger data.

ArcGIS + NumPy {data-background="images/Picture2.jpg"}
--------------

![](images/arcgis-numpy-workflow.png)
 
![](images/logos/matplotlib.png) {data-background="images/Picture2.jpg"}
--------------------------------

 - Plotting library and API for NumPy data
 - [Matplotlib Gallery](http://matplotlib.org/gallery.html){target="_newtab"}

![](images/special-1.png)

![](images/logos/scipy.png) {data-background="images/Picture2.jpg"}
---------------------------

Computational methods for:

 - Integration ([scipy.integrate](http://docs.scipy.org/doc/scipy/reference/tutorial/integrate.html))
 - Optimization ([scipy.optimize](http://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html))
 - Interpolation ([scipy.interpolate](http://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html))
 - Fourier Transforms ([scipy.fftpack](http://docs.scipy.org/doc/scipy/reference/tutorial/fftpack.html))
 - Signal Processing ([scipy.signal](http://docs.scipy.org/doc/scipy/reference/tutorial/signal.html))
 - Linear Algebra ([scipy.linalg](http://docs.scipy.org/doc/scipy/reference/tutorial/linalg.html))
 - Spatial ([scipy.spatial](http://docs.scipy.org/doc/scipy/reference/tutorial/spatial.html))
 - **Statistics** ([scipy.stats](http://docs.scipy.org/doc/scipy/reference/tutorial/integrate.html))
 - **Multidimensional image processing** ([scipy.ndimage](http://docs.scipy.org/doc/scipy/reference/tutorial/ndimage.html))

<div class="notes">
Spatial is the tools across all of the domains of science, very general.

That said, can be useful in a variety of circumstances, e.g. `KDTree` for finding data quickly.
</div>

SciPy: Geometric Mean {data-background="images/Picture2.jpg"}
---------------------

 - Calculating a geometric mean of an _entire raster_ using SciPy ([source](../examples/geometric-mean.py))

![](images/geom-mean.png)

```python
import scipy.stats  
rast_in = 'data/input_raster.tif'
rast_as_numpy_array = arcpy.RasterToNumPyArray(rast_in)
raster_geometric_mean = scipy.stats.stats.gmean(
    rast_as_numpy_array, axis=None)  
```

<div class="notes">
([Inspiration](https://geonet.esri.com/message/436296#436296))
</div>

Use Case: Benthic Terrain Modeler {data-background="images/btm-terrain.jpg"}
--------------------------------

Benthic Terrain Modeler {data-background="images/Picture4.jpg"}
-----------------------

 - A Python Add-in and Python toolbox for geomorphology
 - Open source, can borrow code for your own projects:
   [https://github.com/EsriOceans/btm](https://github.com/EsriOceans/btm)
 - Active community of users, primarily marine scientists, but also useful for other applications 

Lightweight SciPy Integration {data-background="images/Picture4.jpg"}
-----------------------------

 - Using `scipy.ndimage` to perform basic multiscale analysis
 - Using `scipy.stats` to compute circular statistics
 
Lightweight SciPy Integration {data-background="images/Picture4.jpg"}
-----------------------------

[Example source](../examples/calculate-bpi-with-scipy.py)
```python
import arcpy
import scipy.ndimage as nd
from matplotlib import pyplot as plt

ras = "data/input_raster.tif"
r = arcpy.RasterToNumPyArray(ras, "", 200, 200, 0)

fig = plt.figure(figsize=(10, 10))
```

Lightweight SciPy Integration {data-background="images/Picture4.jpg"}
-----------------------------

```python
for i in xrange(25):
    size = (i+1) * 3
    print "running {}".format(size)
    med = nd.median_filter(r, size)

    a = fig.add_subplot(5, 5,i+1)
    plt.imshow(med, interpolation='nearest')
    a.set_title('{}x{}'.format(size, size))
    plt.axis('off')
    plt.subplots_adjust(hspace = 0.1)
    prev = med

plt.savefig("btm-scale-compare.png", bbox_inches='tight')
```

&nbsp; {data-background="images/btm-scale-compare-2.png"}
-

<br>

SciPy Statistics {data-background="images/Picture4.jpg"}
----------------

![](images/aspect-statistical.png)

 - Break down aspect into `sin()` and `cos()` variables
 - Aspect is a circular variable &mdash; without this 0 and 360 are opposites instead of being the same value

SciPy Statistics {data-background="images/Picture4.jpg"}
----------------

Summary statistics from SciPy include circular statistics ([source](../examples/circular-stats.py)).

```python
import scipy.stats.morestats

ras = "data/aspect_raster.tif"
r = arcpy.RasterToNumPyArray(ras)

morestats.circmean(r)
morestats.circstd(r)
morestats.circvar(r)
```

Demo: SciPy {data-background="images/Picture2.jpg"}
-----------



Multidimensional Data {data-background="images/Picture4.jpg"}
=====================

NetCDF4 {data-background="images/Picture4.jpg"}
-------

 * Fast, HDF5 and NetCDF4 read+write support, OPeNDAP
 * Heirarchical data structures
 * Widely used in meterology, oceanography, climate communities
 * Easier: Multidimensional Toolbox, but can be useful

([Source](../examples/netcdf-open.py))
```python
import netCDF4
nc = netCDF4.Dataset('test.nc', 'r', format='NETCDF4')
print nc.file_format
# outputs: NETCDF4
nc.close()
```
<div class="notes">
 * CF compliant data
 * Fast, C-based access 
</div>

Multidimensional Improvements {data-background="images/Picture4.jpg"}
--------------------

 - Multidimensional formats: HDF, GRIB, NetCDF
 - Access via OPeNDAP, vector renderer, Raster Function Chaining
 - [An example which combines mutli-D with time](http://desktop.arcgis.com/en/desktop/latest/manage-data/raster-and-images/creating-and-visualizing-a-multidimensional-mosaic-dataset.htm)
 - Multi-D supported as WMS, and in Mosaic datasets (10.2.1+)


Pandas {data-background="images/Picture2.jpg"}
======

![](images/logos/pandas.png) {data-background="images/Picture2.jpg"}
----------------------------
 - **Pan**el **Da**ta &mdash; like R "data frames"
 - Bring a robust data _analysis_ workflow to Python
 - Data frames are fundamental &mdash; treat tabular (and multi-dimensional)
   data as a labeled, indexed series of observations.

![](images/logos/pandas.png) {data-background="images/Picture2.jpg"}
----------------------------

([Source](../examples/pandas-filter.py))
```python
import pandas

data = pandas.read_csv('data/season-ratings.csv')
data.columns
```
```python
Index([u'season', u'households', u'rank', u'tv_households', \
       u'net_indep', u'primetime_pct'], dtype='object')
```

![](images/logos/pandas.png) {data-background="images/Picture2.jpg"}
----------------------------

```python
majority_simpsons = data[data.primetime_pct > 50]
```
        season households  tv_households  net_indep  primetime_pct
    0        1  13.4m[41]           92.1       51.6      80.751174
    1        2  12.2m[n2]           92.1       50.4      78.504673
    2        3  12.0m[n3]           92.1       48.4      76.582278
    3        4  12.1m[48]           93.1       46.2      72.755906
    4        5  10.5m[n4]           93.1       46.5      72.093023
    5        6   9.0m[50]           95.4       46.1      71.032357
    6        7   8.0m[51]           95.9       46.6      70.713202
    7        8   8.6m[52]           97.0       44.2      67.584098
    8        9   9.1m[53]           98.0       42.3      64.383562
    9       10   7.9m[54]           99.4       39.9      60.916031
    10      11   8.2m[55]          100.8       38.1      57.466063
    11      12  14.7m[56]          102.2       36.8      53.958944
    12      13  12.4m[57]          105.5       35.0      51.094891

Demo: Pandas {data-background="images/Picture2.jpg"}
------------

SymPy {data-background="images/Picture2.jpg"}
=====

![](images/logos/sympy.png){class="tight"} {data-background="images/Picture2.jpg"}
---------------------------

 - A Computer Algebra System (CAS), solve math equations ([source](../examples/sympy-algebra.py))

```python
from sympy import *
x = symbol('x')
eq = Eq(x**3 + 2*x**2 + 4*x + 8, 0)
```

![](images/sympy-eq.png)

```python
solve(eq, x)
```

![](images/sympy-res.png)


Demo: SymPy {data-background="images/Picture2.jpg"}
----------

Where and How Fast? {data-background="images/Picture2.jpg"}
===================

Where Can I Run This? {data-background="images/Picture2.jpg"}
---------------------
 * Now: 
    - ArcGIS Pro (64-bit) [Standalone Python Install for Pro](http://pro.arcgis.com/en/pro-app/arcpy/get-started/installing-python-for-arcgis-pro.htm)
    - 10.4: ArcMap, Server, both 32- and 64- bit environments
        + Both now ship with [Scipy Stack](https://www.scipy.org/about.html) (sans IPython)
    - MKL enabled NumPy and SciPy everywhere
        + <span style="font-size: 0.6em;">Older releases: NumPy: ArcGIS 9.2+, matplotlib: ArcGIS 10.1+, SciPy: 10.4+, Pandas: 10.4+</span>
    - Conda for managing full Python environments, consuming and producing packages
    - With the ArcGIS API for Python! Can run anywhere Python runs.

<div class="notes">
    - SciPy stack is now available across the platform. Try it out, you can build things that will work on your machine and your users machines without additional work.
    - IPython: Let's get this done like yesterday. Had it in the 'upcoming' of last years slide, I'll eat a hat if it isn't in by next DevSummit.
    - Conda session today, Mesquite GH at 4pm.
</div>

How Does It perform? {data-background="images/Picture2.jpg"}
--------------------

 * Built with Intel’s [Math Kernel Library (MKL)](https://software.intel.com/en-us/intel-mkl) and compilers&mdash;highly optimized Fortran and C under the hood. 
 * Automated parallelization for executed code

[MKL Performance Chart](https://4326.us/esri/scipy/mkl-perf){target="_newtab"}

<div class="notes">
Quoting Kevin from last year: Wicked fast. Pandas is fast, scipy functions are fast, and we now enable MKL across the platform for all builds. You write Python, but get best of class performance for free.

Take this graph with a large grain of salt. Realistically, can expect 2-10x improvements in many numerical routines.
</div>


from future import * {data-background="images/Picture4.jpg"}
====================

Opening Doors {data-background="images/Picture4.jpg"}
-------------

 - Machine learning (``scikit-learn``, ``scikit-image``, ...)
 - Deep learning (``theano``, ...)
 - Bayesian statistics (``PyMC``)
    + Markov Chain Monte Carlo (MCMC)
 - Frequentist statistics (``statsmodels``)
 - With Conda, not just Python! ``tensorflow``, many others

Resources {data-background="images/Picture4.jpg"}
=========

Other Sessions {data-background="images/Picture4.jpg"}
--------------

 - [Exploring Continuum Analytics' Open Source Offerings](https://devsummitps17.schedule.esri.com/session-catalog/216814585) &mdash; tomorrow 10:30 in Mesquite G-H
 - [Getting Data Science with R and ArcGIS](https://devsummitps17.schedule.esri.com/session-catalog/1910638256) &mdash; stick around, in this room in 30 min! [2016 video](http://www.esri.com/videos/watch?videoid=5129&channelid=LegacyVideo&isLegacy=true&title=getting-data-science-with-r-and-arcgis)

 - [Integrating Open-source Statistical Packages with ArcGIS](https://devsummitps17.schedule.esri.com/session-catalog/819386409) earlier today, [2016 video](http://www.esri.com/videos/watch?videoid=5074&channelid=LegacyVideo&isLegacy=true&title=integrating-open-source-statistical-packages-with-arcgis)
 - [Harnessing the Power of Python in ArcGIS Using the Conda Distribution](https://devsummit.schedule.esri.com/#schedule/56b287364be5dd46a3000235/56b287364be5dd46a3000236) yesterday, [2016 video](http://www.esri.com/videos/watch?videoid=5072&channelid=LegacyVideo&isLegacy=true&title=harnessing-the-power-of-python-in-arcgis-using-the-conda-distribution)

New to Python {data-background="images/Picture4.jpg"}
-------------

 - Courses:
    + [Programming for Everybody](https://www.coursera.org/course/pythonlearn)
    + [Codecademy: Python Track](http://www.codecademy.com/tracks/python)
 - Books:
    + [Learn Python the Hard Way](http://learnpythonthehardway.org/)
    + [How to Think Like a Computer Scientist](http://interactivepython.org/runestone/static/thinkcspy/toc.html)

GIS Focused {data-background="images/Picture4.jpg"}
-----------

 - [Python Scripting for ArcGIS](http://esripress.esri.com/display/index.cfm?fuseaction=display&websiteID=276&moduleID=0)
 - [ArcPy and ArcGIS - Geospatial Analysis with Python](https://www.packtpub.com/application-development/arcpy-and-arcgis-geospatial-analysis-python)
 - [Python Developers GeoNet Community](https://geonet.esri.com/community/developers/gis-developers/python)
 - [GIS Stackexchange](https://gis.stackexchange.com/)

Scientific {data-background="images/Picture4.jpg"}
----------

 Courses:

 - [Python Scientific Lecture Notes](https://scipy-lectures.github.io)
 - [High Performance Scientific Computing](https://www.coursera.org/course/scicomp)
 - [Coding the Matrix: Linear Algebra through Computer Science Applications](https://www.coursera.org/course/matrix)
 - [The Data Scientist’s Toolbox](https://www.coursera.org/course/datascitoolbox)

Scientific {data-background="images/Picture4.jpg"}
----------

Books:

 - Free:
    + [Probabilistic Programming & Bayesian Methods for Hackers](https://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/)
        + very compelling book on Bayesian methods in Python, uses SciPy + PyMC.
    + [Kalman and Bayesian Filters in Python](https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python)  

Scientific {data-background="images/Picture4.jpg"}
----------
 - Paid: 
    + [Coding the Matrix](http://www.codingthematrix.com/)
        + How to use linear algebra and Python to solve amazing problems.
    + [Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython](http://shop.oreilly.com/product/0636920023784.do)
        + The cannonical book on Pandas and analysis.

Packages {data-background="images/Picture4.jpg"}
--------

Only require SciPy Stack:

 - Scikit-learn:
    + [Lecture material](https://scipy-lectures.github.io/advanced/scikit-learn/index.html)
    + Includes SVMs, can use those for image processing among other things...
 - FilterPy, Kalman filtering and optimal estimation:
    + [FilterPy on GitHub](https://github.com/rlabbe/filterpy)
 - [An extensive list of machine learning packages](https://github.com/svaksha/pythonidae/blob/master/AI.md)

Code {data-background="images/Picture4.jpg"}
----

 - [ArcPy + SciPy on Github](https://github.com/search?p=5&q=scipy+arcpy&type=Code&utf8=%E2%9C%93)
 - [raster-functions](https://github.com/Esri/raster-functions) 
    + An open source collection of function chains to show how to do complex things using NumPy + scipy on the fly for visualization purposes
 - [statistics library](https://docs.python.org/3/library/statistics.html) with a handful of descriptive statistics included in Python 3.4.
- _TIP_: Want a codebase that runs in Python 2 and 3? [Check out future](http://python-future.org), which helps maintain a single codebase that supports both. Includes the `futurize` script to initially a project written for one version.

Scientific ArcGIS Extensions {data-background="images/Picture4.jpg"}
----------------------------

 - [PySAL ArcGIS Toolbox](https://github.com/Esri/PySAL-ArcGIS-Toolbox)
 - [Movement Ecology Tools for ArcGIS (ArcMET)](http://www.movementecology.net/)
 - [Marine Geospatial Ecology Tools (MGET)](http://mgel.env.duke.edu/mget/)
    + Combines Python, R, and MATLAB to solve a wide variety of problems
 - [SDMToolbox](http://sdmtoolbox.org/)
    + species distribution & maximum entropy models
 - [Benthic Terrain Modeler](http://www.arcgis.com/home/item.html?id=b0d0be66fd33440d97e8c83d220e7926)
 - [Geospatial Modeling Environment](http://www.spatialecology.com/gme/)
 - [CircuitScape](http://www.circuitscape.org/)

Conferences {data-background="images/Picture4.jpg"}
-----------

 - [PyCon](http://pycon.org)
    + The largest gathering of Pythonistas in the world
 - [SciPy](https://scipy.org)
    + A meeting of Scientific Python users from all walks
 - [GeoPython](http://www.geopython.net/)
    + The Python event for Python and Geo enthusiasts
 - [PyVideo](http://pyvideo.org/)
    + Talks from Python conferences around the world available freely online.
    + [PyVideo GIS talks](http://pyvideo.org/search?models=videos.video&q=gis)

Closing {data-background="images/Picture2.jpg"}
=======

Thanks {data-background="images/Picture2.jpg"}
------

 - Geoprocessing Team
 - The many amazing contributors to the projects demonstrated here.
    + Get involved! All are on GitHub and happily accept contributions.

Rate This Session {data-background="images/Picture2.jpg"}
-----------------

**iOS, Android**: Feedback from within the app

. . . 

**Windows Phone, or no smartphone?** Cuneiform tablets accepted.

![](images/Amarna_Akkadian_letter_rotated_2.png){style="border: none; background: none; box-shadow: none;"}

<span style="display:none">fin</span> {data-background="images/end.png"}
---

