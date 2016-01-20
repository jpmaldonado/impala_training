[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/repo/summerela/impala_training)

# Impala Training
Training materials for interacting with impala via Hue, impala-shell, R and Python. 

## Introduction
The [impala training](https://github.com/summerela/impala_training/blob/master/Tutorials/impala_training_public.pdf) PDF file is located here if you would like to follow along with the presentation. 

## Hue Interface
The simplest way to interact with impala is via the Hue web interface. This interface is great for viewing database and table structures and provides a nice graphical interface, however, query results on larger data sets are unreliable. 

- [Hue Tutorial](https://github.com/summerela/impala_training/blob/master/Tutorials/using_hue.pdf)  

## Impala Shell 
For working with large tables and results set, the Hue interface can produce unreliable results due to size limits and caching issues. In those cases, you can work with impala from the command line, via the impala-shell.

- [Impala Shell Tutorial](https://github.com/summerela/impala_training/blob/master/impala_shell.ipynb)

## Connecting with Python
Once you have setup an ODBC driver on your local machine, you can easily interact with impala using Python via the [ibis](http://www.ibis-project.org/) or [impyla](https://github.com/cloudera/impyla) modules. Since the Ibis module is still under development, this tutorial will only cover impyla.

- Click on the launch binder icon above  
- [Click on connect_python.ipynb](https://github.com/summerela/impala_training/blob/master/connect_python.ipynb)  

## Connect with R
Once you've created an ODBC DSN on your machine, you can connect to R using the RODBC package. 

- [Connect with R tutorial](https://github.com/summerela/impala_training/blob/master/Tutorials/connect_with_R.md)  
- [Connect with R script](https://github.com/summerela/impala_training/blob/master/connect_R.R)  

## SQL Query Basics
Choose your preferred interface and run through the following tutorial to learn about creating basic SQL queries. 

- [Building Queries](https://github.com/summerela/impala_training/blob/master/Tutorials/building_queries.md)  

## Resources
For more information, here are some helpful links: 

- [SQL](http://www.w3schools.com/sql/default.asp)
- [Impala syntax](http://www.cloudera.com/content/www/en-us/documentation/enterprise/latest/topics/impala_langref.html)
- [RODBC manual](https://cran.r-project.org/web/packages/RODBC/RODBC.pdf)
- [Impala shell](http://www.cloudera.com/content/www/en-us/documentation/archive/impala/2-x/2-1-x/topics/impala_impala_shell.html)
- [Impyla](https://github.com/cloudera/impyla)
- [Ibis](http://www.ibis-project.org/)
- [Optimizing impala queries](http://www.cloudera.com/content/www/en-us/documentation/archive/impala/2-x/2-1-x/topics/impala_performance.html)

## Need help or have questions? 
This tutorial was designed specifically for the ISB/Inova partnership. If you have any questions/comments/corrections/suggestions please feel free to [email me](mailto:selasady@systemsbiology.org).
