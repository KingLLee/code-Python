'''
    nc2binary

    by KingLee 2022.9.24

        the WRF landtype(or soiltype) is saved to binary file. If you need to change them and simulate the LULCC effect to
        the climate, you can use this script to change the WRF default landtype(or soiltype) data. So, the common nc data can
        be converted into the binary data.
'''

import numpy as np
import xarray as xr


#%% Set nc path and var name manually
filepath = './bnu_soiltype_bot.nc'

data = xr.open_dataset(filepath)

var_name = 'bnu_soiltype_bot'


#%% read the data
var = np.array(data[var_name])
lat = np.array(data['lat'])
lon = np.array(data['lon'])


#%% create all the binary data file name, and set the target path where the data is storaged.
filename = []
target_path = './manully/'
for ilon in np.arange(36):
    for ilat in np.arange(18):
        lonsta = str(1+1200*(ilon)).zfill(5)
        lonend = str(1200*(ilon+1)).zfill(5)
        latsta = str(1+1200*(ilat)).zfill(5)
        latend = str(1200*(ilat+1)).zfill(5)
        filename.append(target_path+f'{lonsta}-{lonend}.{latsta}-{latend}')



#%% separate the array to tiles and save them to binary file respectively.
for ilon in np.arange(36):
    for ilat in np.arange(18):

        i = ilon*18 + ilat
        
        print(i)
        lonsta = 1200*(ilon)
        lonend = 1200*(ilon+1)-1

        latsta = 1200*(ilat)
        latend = 1200*(ilat+1)-1

        array = var[lonsta:lonend+1, latsta:latend+1]

        array = np.rot90(array, 1)

        array = np.flip(array, axis=0)
        
        array.tofile(filename[i])