import os

# Set environment variable GRASSBIN to the path to the grass executable
os.environ['GRASSBIN']= r'C:\OSGeo4W\bin\grass78.bat'

from grass_session import Session
from grass.script import core as gcore
import grass.script as gscript
import grass.script.setup as gsetup
# import python grass libraries
from grass.pygrass.modules.shortcuts import general as g
from grass.pygrass.modules.shortcuts import raster as r
from grass.pygrass.modules.shortcuts import vector as v
from grass.pygrass.modules.shortcuts import temporal as t

# define path to grassdata folder
mygisdb = 'C:\\Users\\barto\\Documents\\grassdata'
mylocation = 'copenhagen'
mymapset = 'PERMANENT'

# set up grass session
user = Session()
user.open(gisdb=mygisdb, location=mylocation, mapset=mymapset, create_opts='EPSG:25832')

folder = r"C:\Users\barto\Documents\Projekter\hvorio\plads-i-solen\data\surface_model"
print(folder)
for index, file in enumerate(folder):
    print(file,index)
    r.import(input=file, output=file, overwrite=True)
    if index == 10:
        break

# close grass session
user.close()
