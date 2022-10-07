
'''
    Binary to NC 
    
        By KingLee 2022.9.24

        the WRF landtype(or soiltype) is saved to binary file, and it is convenient to convert the binary 
        data to array data, so you can process them easily by using python script. Here is an example
        to convert the wrf binary file to nc file.
'''

import numpy as np
import xarray as xr



## Read the binary tile to array by using numpy.fromfile
def bnu_read_Binary(filename):
    '''
        :param  filename:  the input data's  '/path/filename'
        :return: bdata: 2D-array
    '''
    # Read the binary data to 1D-array, please noted the single charactor length, and change the 'np.int8' 
    # to another one if needed.
    with open(filename) as f:
        rectype = np.dtype(np.int8)
        bdata = np.fromfile(f, dtype=rectype)
    
    # Reshape the data to a 2D-array, and if (1200, 1200) is changed, the specific params should be changed too.
    bdata = bdata.reshape([1200, 1200]) 

    # Reverse the order of elements in an array along the given axis.
    bdata = np.flip(bdata, axis=0)

    # the data's dimension is given by (lat, lon)
    return bdata


## Export the var array to the Netcdf file
def Build_nc_template(lat, lon, z, var_name, filepath):
    
    # Build the dataset
    ds = xr.Dataset(
        {f"{var_name}" : (["lon", "lat"], z )},
        coords={
            "lat" : lat,
            "lon" : lon,
        }
    )
    # Save the dataset
    ds.to_netcdf(filepath)


#%% Create the lat and lon var.
lat = np.arange(-89.99583, 90, 0.00833333, dtype=np.float64)
lon = np.arange(-179.99583, 180, 0.00833333, dtype=np.float64)


#%% Integrate the filename in an order. You should change the data path to a correct one.
filename = []
for ilon in np.arange(36):
    for ilat in np.arange(18):
        lonsta = str(1+1200*(ilon)).zfill(5)
        lonend = str(1200*(ilon+1)).zfill(5)
        latsta = str(1+1200*(ilat)).zfill(5)
        latend = str(1200*(ilat+1)).zfill(5)
        filename.append(f'./{lonsta}-{lonend}.{latsta}-{latend}')


#%%  read every file in the list 'filename' and concatenate them into an array
read_data = np.zeros([np.size(lon), np.size(lat)], dtype=np.int8)

for ilon in np.arange(36):  # 36 or 18 belongs to how many tiles along the lon and lat seperately.
    for ilat in np.arange(18):

        i = ilon*18 + ilat
        print(i)

        lonsta = 1200*(ilon)
        lonend = 1200*(ilon+1)-1

        latsta = 1200*(ilat)
        latend = 1200*(ilat+1)-1


        array = bnu_read_Binary(filename[i])

        
        # convert the data's dimension to (lon, lat)
        read_data[lonsta:lonend+1, latsta:latend+1] = np.rot90(array, -1)


#%% save the array to nc file. 
# You should give the var_name and file path. Default filepath is your script's path.
var_name = 'modis_landuse_20class_30s_with_lakes'
filepath = f"{var_name}.nc"

Build_nc_template(lat, lon, read_data, var_name, filepath)