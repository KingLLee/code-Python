"""
Obtain the shape file's mask
    by King Lee 2022.9.3
    When you draw the 2D regional distribution of the meterological data (e.g. Geopotential height, specific humidity), 
you would like to highlight the region you want to show to your audience. And you will be pleased to mask out other regions, 
so this code would be in line with your requirements.
"""


import numpy as np
import xarray as xr
import cv2
import shapefile


# Obtain region mask_out 
def mask_region(region_shpfile, lat, lon):
    '''
    Obtain region mask array
    This code will output a region array which satisfies your resolution by using your lat&lon array. 
        :param region_shpfile: the specific path of the region .shp
        :param lat:            each grids latitude vector
        :param lon:            each grids longitude vector
        :return
                mask_array: In region: 1
                            On region: 0
                            Out region: -1
    Attention Please:
                      Many shape file(.shp) like Zhejiang Province have many independent island, and the var prt in this code 
                      will give a clear mark that the code should distinguish different islands in specific location. There I 
                      choose the last location, because I just want to mask the most important part of the region. And if you 
                      need more part of the region, you can open up the code below. 
                      What's more, try to save the mask_array if you use the high resolution, and ultimately save your time
                      running the code again and again.
                      Thanks a lot.
    '''
    region = shapefile.Reader(region_shpfile)
    border = region.shapes()
    border_points = border[0].points
    prt = np.array(border[0].parts)
    countour = np.array(border_points).astype(np.float32)[prt[-1]::, :]

    mask_array = np.zeros([np.size(lat), np.size(lon)]) #, np.size(prt)])
    for i in np.arange(np.size(lat)):
        print(i)
        for j in np.arange(np.size(lon)):
            point = (lon[j], lat[i])
            mask_array[i, j] = cv2.pointPolygonTest(countour, point, False)
    mask_array = mask_array.astype(int)
    return mask_array
''' 
    for i in np.arange(np.size(lat)):
        print(i)
        for j in np.arange(np.size(lon)):
            point = (lon[j], lat[i])
            for K in np.arange(np.size(prt)):
                if K==np.size(prt)-1:
                    part_countour = courtour[prt[K]::, :]
                    jilin_mask[i, j, K] = cv2.pointPolygonTest(part_countour, point, False)
                
                else:
                    part_countour = courtour[prt[K]:prt[K+1], :]
                    jilin_mask[i, j, K] = cv2.pointPolygonTest(part_countour, point, False)
                '''
    #jilin_mask = jilin_mask.astype(int)
    #return jilin_mask
 

# Example
if __name__ == "__main__":
    lat = np.linspace(20, 1, 40, endpoint=True)
    lon = np.linspace(120, 1, 140, endpoint=True)
    region_shpfile = 'zhejiang_province.shp'
    zhejiang_mask = mask_region(region_shpfile, lat, lon)
