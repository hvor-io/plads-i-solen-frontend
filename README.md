# En plads i solen 

<img src="https://placekitten.com/g/120/178" align="right"
     alt="" width="120" height="178">

En plads i solen (a spot in the sun) is an application mainly built with Python. It calculates shadows on the 
landsacpe on a given day in Copenhagen. This can be used to give an indication of where you can soak up the sun. 

In addition to Python the following tools are used:

* GRASS GIS
* A server with Linux installed (Digital Ocean in this instance)
* An installation of geoserver

<p align="center">
  <img src="https://placekitten.com/g/400" alt="" width="400">
</p>

## How the application is used

## Hvad er den til for?

## Inputs and necessary stuff

1. An elevation model. To be precise a DTM not a DSM
2. GRASS GIS
3. Patience

## Future developments

1
2
3


## Sådan virker den


1. 
2.
...
  
## Usage

## BUGS
###
Had GRASS installed through OSGEO. Uninstalled it and installed it through the GRASS website.

###
Had to add C:\OSGeo4W\apps\grass\grass78\lib to the \$PATH\$ as it could not find the relevant dlls. 

### 
Had trouble with parsing the GRASSBIN env variable. Had to add '" "' to ensure interpreting as a string.
