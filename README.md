[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/repo/summerela/impala_training)

# Impala Training
Training materials for interacting with impala via Hue, impala-shell, R and Python. 

## Introduction
The [impala training](https://github.com/summerela/impala_training/blob/master/impala_training_public.pdf) PDF file was designed to walk you through all of the following tutorials. 

## Hue Interface
The simplest way to interact with impala is via the Hue web interface. This interface is great for viewing database and table structures and provides a nice graphical interface, however, query results on larger data sets are unreliable. 

- [Hue Tutorial](https://github.com/summerela/impala_training/blob/master/using_hue.pdf)  

## Impala Shell 
For working with large tables and results set, the Hue interface can produce unreliable results due to size limits and caching issues. In those cases, you can work with impala from the command line, via the impala-shell.

- [Impala Shell Tutorial](https://github.com/summerela/impala_training/blob/master/impala_shell.ipynb)

## Connecting with Python
Once you have setup an ODBC driver on your local machine, you can easily interact with impala using Python via the [ibis](http://www.ibis-project.org/) or [impyla](https://github.com/cloudera/impyla) modules. Since the Ibis module is still under devlopment, this tutorial will only cover impyla.

- Click on the launch binder icon above  
- [Click on connect_python.ipynb](https://github.com/summerela/impala_training/blob/master/connect_python.ipynb)  

## Connect with R
Once you've created an ODBC DSN on your machine, you can connect to R using the RODBC package. 

- [Connect with R tutorial](https://github.com/summerela/impala_training/blob/master/connect_with_R.md)  
- [Connect with R script](https://github.com/summerela/impala_training/blob/master/connect_R.R)  

## SQL Query Basics
Choose your prefered interface and run through the following tutorial to learn about creating basic SQL queries. 

- [Building Queries](https://github.com/summerela/impala_training/blob/master/building_queries.md)  

## Sample Pipeline
You can try out the following sample pipeline in python to locate, filter and annotate a set of variants. 

- Click on the launch binder icon above (unless you already have it running)
- [Sample Pipeline](https://github.com/summerela/impala_training/blob/master/variant_pipeline_python.ipynb)

## Need help of have questions? 
This tutorial was designed specifically for the ISB/Inova partnership. If you have any questions/comments/corrections/suggestions please feel free to email me at Summer dot Elasady AT systemsbiology.org
