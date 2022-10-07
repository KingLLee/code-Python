'''
Drawing series: Regional contourf draw

    by KingLee 2022.10.6

    A series of drawing methods to present specific data in a picture as quick as you can.

    This is for regional contourf picture. You can use it cooperating with the Methods: Shape_Mask, so that
    the pic would just present the region you prefer.
'''


import numpy as np
import cartopy.mpl.ticker as cticker
import cartopy.crs as ccrs
from matplotlib.ticker import MultipleLocator
import cmaps
import cartopy.io.shapereader as shpreader


def region_contourf_draw(lon, lat, z, levels, shape_file, img_extent, fig_axe):
    '''
        :param lon: longitude vector
        :param lat: latitude vector
        :param   z: varible matrix, (lat, lon)
        :param levels: It is the colorbar parameter - levels. You can adjust your
                        levels which would be suitable for your data. Also, from 
                        setting the levels number, you would change the colorbar 
                        total color number, which will help you to oberseve and 
                        anylise your pic more clearly. 
        :shape_file: Shape file(.shp) Path. The specific region. 
        :img_extent: the region's spacial scale. It's a list, including [leftlon, rightlon, lowerlat, upperlat]
        :fig_axe: Artificially set the canvas by matplotlib.
    '''

    region_shp = shape_file

    img_extent = img_extent

    leftlon, rightlon, lowerlat, upperlat = img_extent
    xstep, xmajor_step, xminor_step = 4, 4, 1  # set the x-axis step
    ystep, ymajor_step, yminor_step = 4, 4, 1  # set the y-axis step
    proj = ccrs.PlateCarree()

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

    fig_axe.add_geometries(shpreader.Reader(region_shp).geometries(), proj, facecolor = 'none', edgecolor = 'k', linewidth = 2, zorder = 999)


    fig_axe.contourf(lon, lat, z, levels = levels, transform = ccrs.PlateCarree(), cmap = cmaps.NCV_jet)