'''
    Situ 1D-data to Grid 2D-data

        by KingLee 2022.10.11

        There is often observation data or other situ flux data, which are not in grid format, so it's difficult to draw the contourf figure by using
        1D situ data. This function can solve this problem by transform the 1D situ data to 2D grid data.
'''

import numpy as np


def situ_to_grid(lat_situ, lon_situ, situ_value):
    '''
    :param lat_situ:  1D situ lat vector
    :param lon_situ:  1D situ lon vector
    :situ_value:  1D situ value vector
    :return
            lat_grid:  1D lat vector
            lon_grid:  1D lon vector
            grid_value:  2D matrix, and except the situ data, other data is None.
            site:  Some situ data may have lots of levels, like argo data, we should transform different levels to grid data, and finally form a 3D grid data,
                    in order to have the convenience to deal with levels, you can use site to create grids in different levels. 
    '''

    grid_value = np.full([np.size(lat_situ), np.size(lon_situ)], np.nan)
    lat_grid = np.sort(lat_situ)
    lon_grid = np.sort(lon_situ)
    site = np.zeros([np.size(lat_situ), 2])
    for i in np.arange(np.size(situ_value)):
        lat_site = np.argwhere(lat_grid==lat_situ[i])[0][0]
        lon_site = np.argwhere(lon_grid==lon_situ[i])[0][0]
        
        site[i, 0] = lat_site
        site[i, 1] = lon_site

        grid_value[lat_site, lon_site] = situ_value[i]
    
    return lat_grid, lon_grid, grid_value, site