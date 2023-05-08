import pysolar
import datetime
import subprocess
import os
import sys

loc_n = 55.673049
loc_s = 12.575681

# current folder
BASE_DIR = os.path.join( os.path.dirname( __file__ ), '..' )

# Access data/surface_model folder
os.chdir(BASE_DIR + "/data/surface_model")

# year, month, day, hour, minute, second, microsecond, tzinfo
startdate = datetime.datetime(2022, 1, 1, 12, 0, 0, 0, tzinfo=datetime.timezone.utc)

# get shadow length
def get_shadow_length(lat, lon, date, time):
    alt = pysolar.solar.get_altitude(lat, lon, date, time)
    if alt > 0:
        return 0
    else:
        return -alt * 1000 / pysolar.solar.get_altitude(loc_n, loc_s, date, time)
        
# get azimuth
def get_azimuth(lat, lon, date):
    return pysolar.solar.get_azimuth(lat, lon, date)

# get altitude
def get_altitude(lat, lon, date):
    return pysolar.solar.get_altitude(lat, lon, date)


# run gdal hillshade with subprocess
def run_hillshade(dem, az, alt):
    print(dem)
    subprocess.run(["gdaldem", "hillshade","{0}".format(dem), "{0}_hillshade.tif".format(dem)])


while startdate.year == 2022:
    az, alt = get_azimuth(loc_n, loc_s, startdate), get_altitude(loc_n, loc_s, startdate)
    print(az, alt)
    for file in os.listdir(os.getcwd()):
        print(os.getcwd() + "/" + file)
        file = os.getcwd() + "/" + file
        # check if file extension is tif
        if file.endswith(".tif"):
            run_hillshade(file, az, alt)
            # move file to shadow folder
            #os.rename(file, "../shadow/" + file)
            # move hillshade file to shadow folder
            #os.rename(file + "_hillshade.tif", "../shadow/" + file + "_hillshade.tif")
            # move shadow length file to shadow folder
            #os.rename("shadow_length.txt", "../shadow/" + file + "_shadow_length.txt")
            break
    break
    startdate += datetime.timedelta(hours=1)
