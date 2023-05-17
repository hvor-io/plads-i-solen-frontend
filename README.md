# plads-i-solen
En applikation der viser hvor der er mest skygge og sol i København 

## BUGS
###
Had GRASS installed through OSGEO. Uninstalled it and installed it through the GRASS website.

###
Had to add C:\OSGeo4W\apps\grass\grass78\lib to the \$PATH\$ as it could not find the relevant dlls. 

### 
Had trouble with parsing the GRASSBIN env variable. Had to add '" "' to ensure interpreting as a string.