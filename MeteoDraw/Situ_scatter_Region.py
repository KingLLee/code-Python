'''
    region_Situ_draw

        by KingLee 2022.10.11

        A series of drawing methods to present specific data in a picture as quick as you can.
        
        This function can give a quick look of the situ position and situ value distribution.
'''

import numpy as np
import cartopy.mpl.ticker as cticker
import cartopy.crs as ccrs
from matplotlib.ticker import MultipleLocator
import cmaps
import cartopy.io.shapereader as shpreader
import cartopy.feature as cfeature

def region_situ_draw(lon, lat, z, shape_file, img_extent, fig_axe):
    '''
        :param lon: longitude vector
        :param lat: latitude vector
        :param   z: 1D-varible vector,
        :shape_file: Shape file(.shp) Path, the specific region. The code below also inludes the  COASTLINE and OCEAN features, and default is not using 
                    the shape file. 
        :img_extent: the region's spacial scale. It's a list, including [leftlon, rightlon, lowerlat, upperlat]
        :fig_axe: Artificially set the canvas by matplotlib.
    '''

    region_shp = shape_file

    img_extent = img_extent

    leftlon, rightlon, lowerlat, upperlat = img_extent
    xstep, xmajor_step, xminor_step = 10, 10, 2  # set the x-axis step
    ystep, ymajor_step, yminor_step = 10, 10, 2  # set the y-axis step
    proj = ccrs.PlateCarree()

    # fig_axe.add_feature(cfeature.OCEAN)
    fig_axe.set_xticks(np.arange(leftlon, rightlon + xstep, xstep), crs = proj)
    fig_axe.set_yticks(np.arange(lowerlat, upperlat + ystep, ystep), crs = proj)

    longitude = cticker.LongitudeFormatter(zero_direction_label = False, degree_symbol = '')
    latitude = cticker.LatitudeFormatter(degree_symbol = '')
    fig_axe.xaxis.set_major_formatter(longitude)
    fig_axe.yaxis.set_major_formatter(latitude)

    fig_axe.set_extent(img_extent, crs = proj)
    
    xmajorLocator = MultipleLocator(xmajor_step)  # x-axis major tick step length
    xminorLocator = MultipleLocator(xminor_step)  # x-axis minor tick step length
    ymajorLocator = MultipleLocator(ymajor_step)  # y-axis major tick step length
    yminorLocator = MultipleLocator(yminor_step)  # y-axis minor tick step length

    fig_axe.xaxis.set_major_locator(xmajorLocator)
    fig_axe.xaxis.set_minor_locator(xminorLocator)
    fig_axe.yaxis.set_major_locator(ymajorLocator)
    fig_axe.yaxis.set_minor_locator(yminorLocator)

    fig_axe.tick_params(which = 'major', length = 8, width = 1.5)  # Set the major tick properties.
    fig_axe.tick_params(which = 'minor', length = 4, width = 1)  # Set the minor tick properties.
    # fig_axe.tick_params(which = 'major', top=True, right = True)  # Set which axis to display the major tick
    # fig_axe.tick_params(which = 'minor', top=True, right = True)  # Set which axis to display the minor tick

    [x.set_linewidth(1.5) for x in fig_axe.spines.values()]
    [x.set_color("black") for x in fig_axe.spines.values()]
    
    fig_axe.add_feature(cfeature.COASTLINE)
    fig_axe.add_feature(cfeature.OCEAN)
    # fig_axe.add_geometries(shpreader.Reader(region_shp).geometries(), proj, facecolor = 'none', edgecolor = 'k', linewidth = 2, zorder = 999)
    
    # Draw the point with value. If you just need to draw the situ specific position, pls change "c=z" to "c='specific color'"
    S = 10
    fig_axe.scatter(lon, lat, c=z, s=S, marker='o', cmap='jet', transform=ccrs.PlateCarree())
